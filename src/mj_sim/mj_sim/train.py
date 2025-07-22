import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import subprocess
import argparse
import ast
from tqdm import tqdm
import numpy as np

from config.configuration import ModelFitConfig as Conf
from gp_model.gp_common import GPDataset, restore_gp_regressors, read_dataset
from gp_model.utils import sample_random_points
from gp_model.utils import safe_mkdir_recursive, load_pickled_models
from gp_model.utils import distance_maximizing_points, get_model_dir_and_file
from gp_model.gp import CustomKernelFunctions as npKernelFunctions
from gp_model.gp import CustomGPRegression as npGPRegression
from gp_model.gp import GPEnsemble
from gp_model.gp_common import GPDataset, restore_gp_regressors, read_dataset
from gp_model.gp_visualization import gp_visualization_experiment
import time


def gp_train_and_save(x, y, gp_regressors, save_model, save_file, save_path, y_dims, cluster_n, progress_bar=True):
    """
    Trains and saves the 'm' GP's in the gp_regressors list. Each of these regressors will predict on one of the output
    variables only.

    :param x: Feature variables for the regression training. A list of length m where each entry is a Nxn dataset, N is
    the number of training samples and n is the feature space dimensionality. Each entry of this list will be used to
    train the respective GP.
    :param y: Output variables for the regression training. A list of length m where each entry is a N array, N is the
    number of training samples. Each entry of this list will be used as ground truth output for the respective GP.
    :param gp_regressors: List of m GPRegression objects (npGPRegression or skGPRegression)
    :param save_model: Bool. Whether to save the trained models or not.
    :param save_file: Name of file where to save the model. The 'pkl' extension will be added automatically.
    :param save_path: Path where to store the trained model pickle file.
    :param y_dims: List of length m, where each entry represents the state index that corresponds to each GP.
    :param cluster_n: Number (int) of the cluster currently being trained.
    :param progress_bar: Bool. Whether to visualize a progress bar or not.
    :return: the same list as te input gp_regressors variable, but each GP has been trained and saved if requested.
    """

    # If save model, generate saving directory
    if save_model:
        safe_mkdir_recursive(save_path)
    print(save_file)
    print(save_path)

    if progress_bar:
        print("Training {} gp regression models".format(len(y_dims)))
    prog_range = tqdm(y_dims) if progress_bar else y_dims

    for y_dim_reg, dim in enumerate(prog_range):

        # Fit one regressor for each output dimension
        gp_regressors[y_dim_reg].fit(x[y_dim_reg], y[y_dim_reg])
        if save_model:
            full_path = os.path.join(save_path, save_file + '_' + str(dim) + '_' + str(cluster_n) + '.pkl')
            gp_regressors[y_dim_reg].save(full_path)

    return gp_regressors

if __name__ == "__main__":

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--x', nargs='+', type=int, default=[7],
    #                     help='Regression X variables. Must be a list of integers between 0 and 12. Velocities xyz '
    #                             'correspond to indices 7, 8, 9.')

    # parser.add_argument("--y", type=int, default=7,
    #                     help="Regression Y variable. Must be an integer between 0 and 12. Velocities xyz correspond to"
    #                             "indices 7, 8, 9.")

    # input_arguments = parser.parse_args()

    # # Use vx, vy, vz as input features
    # x_feats = input_arguments.x #这里只包括一个维度
    # u_feats = []

    # Regression dimension

    git_version = ''
    try:
        git_version = subprocess.check_output(['git', 'describe', '--always']).strip().decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(e.returncode, e.output)
    print("The model will be saved using hash: %s" % git_version)

    model_name = "simple_sim_gp"
    quad_sim_options = Conf.ds_metadata
    gp_name_dict = {"git": git_version, "model_name": model_name, "params": quad_sim_options}
    print(gp_name_dict)
    # Conf.ds_metadata
    save_file_path, save_file_name = get_model_dir_and_file(gp_name_dict)
    print(save_file_name)
    print(save_file_path)

    dataset_name = Conf.ds_name
    # x_features = [0, 1, 2] #这里只包括一个维度 x x_dot f
    # x_features = [3, 4, 5] #这里只包括一个维度 x x_dot f
    # x_features = [6, 7, 8] #这里只包括一个维度 x x_dot f
    # u_features = []
    # reg_y_dim = 2  #表示只回归力
    # reg_y_dim = 5  #表示只回归力
    # reg_y_dim = 8  #表示只回归力

    X_features = [[0, 1, 2],
                  [3, 4, 5]]
    U_features = [[0, 6],  # k ,d
                  [1, 7]]  # k ,d
    # U_features = [[],
    #               []]
    Reg_y_dim = [2, 5]

    histogram_pruning_bins = Conf.histogram_bins
    histogram_pruning_threshold = Conf.histogram_threshold
    x_value_cap = Conf.velocity_cap  #后处理参数，待定

    for item in range(2):
        x_features = X_features[item]
        u_features = U_features[item]
        reg_y_dim = Reg_y_dim[item]

        if isinstance(dataset_name, str):
            df_train = read_dataset(dataset_name, True, quad_sim_options) # pandas 类型的表格数据
        
            # value = df_train.loc[1, 'state_in_vel']
            # if isinstance(value, str):
            #     value = ast.literal_eval(value)  # 安全地将字符串解析为列表
            #     print("----")
            # print(df_train.head())
            # print(df_train.columns)  # 查看列名
            # print(df_train.loc[0, 'state_in_pose'])  # 检查预期值
            df_train = df_train[:-1] #舍弃最后一行

            gp_dataset = GPDataset(df_train, x_features, u_features, reg_y_dim,
                                    cap=x_value_cap, n_bins=histogram_pruning_bins, thresh=histogram_pruning_threshold, visualize_data=False) #获取数据集的对象

        n_clusters = Conf.clusters
        load_clusters = Conf.load_clusters
        visualize_data = Conf.visualize_data
        gp_dataset.cluster(n_clusters, load_clusters=load_clusters, save_dir=save_file_path, visualize_data=visualize_data) #数据聚类，已经得到了可以用于训练的原始数据

        gp_regressors = []

        # Prior parameters
        sigma_f = 0.5
        length_scale = .1
        sigma_n = 0.01
        n_restarts = 10

        gp_params = {"x_features": x_features, "u_features": u_features, "reg_dim": reg_y_dim,
                        "sigma_n": sigma_n, "n_restarts": n_restarts}

        # Get all cluster centroids for the current output dimension
        centroids = gp_dataset.centroids
        print("Training {} cluster model(s)".format(n_clusters))

        n_train_points = 15
        dense_gp = None #没用
        visualize_model = Conf.visualize_training_result


        range_vec = tqdm(range(n_clusters))  #range_vec 是一个 tqdm 迭代器对象，可以像普通 range 一样用于 for 循环，但会显示进度条

        # print(range_vec)

        for cluster in range_vec: #cluster是数字

            # #### TRAINING POINT SELECTION #### #
            # range_vec.set_description(f"Cluster:{cluster}")

            cluster_mean = centroids[cluster]
            cluster_x_points = gp_dataset.get_x_error(cluster=cluster) #索引出对应的簇的数据
            cluster_y_points = gp_dataset.get_y(cluster=cluster)  #y数据
            cluster_u_points = gp_dataset.get_u(cluster=cluster)  #空

            print(cluster_x_points.shape)
            print(cluster_y_points.shape)
            print(cluster_u_points.shape)
            print("-----------------")

            # range_vec.set_postfix({
            #     'X': str(cluster_x_points.shape),
            #     'Y': str(cluster_y_points.shape),
            #     'U': str(cluster_u_points.shape)
            # })
            # time.sleep(1)

            # Select a base set of training points for the current cluster using PCA that are as separate from each
            # other as possible 对数据集进行了离散化采样，缩小数据集
            selected_points = distance_maximizing_points(
                cluster_x_points, cluster_mean, n_train_points=n_train_points, dense_gp=dense_gp, plot=False)
            
            cluster_y_mean = np.mean(cluster_y_points, 0)

            # # If no dense_gp was provided to the previous function, training_points will be the indices of the training
            # # points to choose from the training set
            if dense_gp is None:
                x_train = cluster_x_points[selected_points] #筛选后的数据集
                y_train = np.squeeze(cluster_y_points[selected_points]) #np.squeeze() 是 NumPy 提供的一个函数，用于移除数组中长度为 1 的维度（即“压缩”数组）
                training_points = selected_points
            else:
                # Generate a new dataset of synthetic data composed of x and y values
                x_mock = np.zeros((13, selected_points.shape[1]))
                if x_features:
                    x_mock[np.array(x_features), :] = selected_points[:len(x_features)]
                u_mock = np.zeros((4, selected_points.shape[1]))
                if u_features:
                    u_mock[np.array(u_features), :] = selected_points[len(x_features):]
                out = dense_gp.predict(x_mock, u_mock)
                out["pred"] = np.atleast_2d(out["pred"])
                y_train = np.squeeze(out["pred"][np.where(dense_gp.dim_idx == reg_y_dim)])
                x_train = selected_points.T
                training_points = []
            # print(x_train.shape[0])
            # # Check if we still haven't used the entirety of the available points，
            # 造成点数不够的原因是因为：        
            # n_clusters = max(int(n_train_points / 10), 30) #簇数取 1/10 或至少 30，确保分布广泛；采样数分配均匀
            # n_samples = int(np.floor(n_train_points / n_clusters)) #每个簇的样本数量
            # 因为整数取整操作，导致n_samples * n_clusters != 50

            n_used_points = x_train.shape[0]
            if n_used_points < n_train_points and n_used_points < cluster_x_points.shape[0]:

                missing_pts = n_train_points - n_used_points
                # 补充采样点
                training_points = sample_random_points(cluster_x_points, training_points, missing_pts, dense_gp)
                if dense_gp is None:
                    # Transform from cluster data index to full dataset index
                    x_train = cluster_x_points[training_points]
                    y_train = np.squeeze(cluster_y_points[training_points])
                    print("x_train", len(x_train))
                else:
                    # Generate a new dataset of synthetic data composed of x and y values
                    training_points = training_points.astype(int)
                    x_mock = np.zeros((13, len(training_points)))
                    if x_features:
                        x_mock[np.array(x_features), :] = cluster_x_points[training_points, :len(x_features)].T
                    u_mock = np.zeros((4, len(training_points)))
                    if u_features:
                        u_mock[np.array(u_features), :] = cluster_u_points[len(x_features):]
                    out = dense_gp.predict(x_mock, u_mock)
                    y_additional = np.squeeze(out["pred"][np.where(dense_gp.dim_idx == reg_y_dim)])
                    y_train = np.append(y_train, y_additional)
                    x_train = np.concatenate((x_train, cluster_x_points[training_points, :len(x_features)]), axis=0)


            # print(x_train.shape)
            # print(y_train.shape)
            # #### GP TRAINING ####
            # Multidimensional input GP regressors
            l_scale = length_scale * np.ones((x_train.shape[1], 1))

            cluster_mean = centroids[cluster]
            gp_params["mean"] = cluster_mean
            gp_params["y_mean"] = cluster_y_mean

            # Train one independent GP for each output dimension
            exponential_kernel = npKernelFunctions('squared_exponential', params={'l': l_scale, 'sigma_f': sigma_f})
            gp_regressors.append(npGPRegression(kernel=exponential_kernel, **gp_params))
            gp_regressors[cluster] = gp_train_and_save([x_train], [y_train], [gp_regressors[cluster]], True, save_file_name,
                                                        save_file_path, [reg_y_dim], cluster, progress_bar=False)[0]



        if visualize_model:
            gp_ensemble = GPEnsemble()
            gp_ensemble.add_model(gp_regressors)
            x_features = x_features
            gp_visualization_experiment(quad_sim_options, gp_dataset,
                                        x_value_cap, histogram_pruning_bins, histogram_pruning_threshold,
                                        x_features, u_features, reg_y_dim,
                                        grid_sampling_viz=True, pre_set_gp=gp_ensemble)



