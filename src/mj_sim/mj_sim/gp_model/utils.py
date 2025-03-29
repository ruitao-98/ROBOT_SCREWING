import os
import math
import json
import errno
import shutil
import joblib
import random
import numpy as np
import casadi as cs
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.interpolate.interpolate import interp1d
import matplotlib.pyplot as plt
import xml.etree.ElementTree as XMLtree
from config.configuration import DirectoryConfig as GPConfig
import pyquaternion

def safe_mkdir_recursive(directory, overwrite=False): #如果路径有多级（如 "a/b/c"），会逐级创建
    if not os.path.exists(directory):
        try:
            os.makedirs(directory) 
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(directory):
                pass
            else:
                raise
    else:
        if overwrite:
            try:
                shutil.rmtree(directory)
            except:
                print('Error while removing directory: {0}'.format(directory))


def safe_mknode_recursive(destiny_dir, node_name, overwrite):
    safe_mkdir_recursive(destiny_dir)
    file_path = os.path.join(destiny_dir, node_name)
    if overwrite and os.path.exists(file_path):
        os.remove(file_path)
    if not os.path.exists(file_path):
        os.mknod(file_path)
        return False  # 文件新建
    return True  # 文件已存在


def jsonify(array):
    if isinstance(array, np.ndarray):
        return array.tolist()
    if isinstance(array, list):
        return array
    return array

def undo_jsonify(array):
    x = []
    for elem in array:
        a = elem.split('[')[1].split(']')[0].split(',')
        a = [float(num) for num in a]
        x = x + [a]
    return np.array(x)


def get_data_dir_and_file(ds_name, training_split, params, read_only=False):
    """
    Returns the directory and file name where to store the next simulation-based dataset.
    """

    # Data folder directory
    rec_file_dir = GPConfig.DATA_DIR

    # Look for file
    f = []
    d = []
    for (dir_path, dir_names, file_names) in os.walk(rec_file_dir):
        f.extend(file_names)
        d.extend(dir_names)
        break

    split = "train" if training_split else "test"

    # Check if current dataset folder already exists. Create it otherwise
    if ds_name in d and os.path.exists(os.path.join(rec_file_dir, ds_name, split)):
        dataset_instances = []
        for (_, _, file_names) in os.walk(os.path.join(rec_file_dir, ds_name, split)):
            dataset_instances.extend([file.split('.csv')[0] for file in file_names])
    else:
        if read_only:
            return None
        safe_mkdir_recursive(os.path.join(rec_file_dir, ds_name, split))
        dataset_instances = []

    json_file_name = os.path.join(rec_file_dir, 'metadata.json')
    if not f:
        if read_only:
            return None
        # Metadata file not found -> make new one
        with open(json_file_name, 'w') as json_file:
            ds_instance_name = "dataset_001"
            json.dump({ds_name: {split: {ds_instance_name: params}}}, json_file, indent=4)
    else:
        # Metadata file existing
        with open(json_file_name) as json_file:
            metadata = json.load(json_file)

        # Check if current dataset name with data split exists in metadata:
        if ds_name in metadata.keys() and split in metadata[ds_name].keys():
            existing_instance_idx = -1
            for i, instance in enumerate(dataset_instances):
                if metadata[ds_name][split][instance] == params:
                    existing_instance_idx = i
                    if not read_only:
                        print("This configuration already exists in the dataset with the same name.")

            if existing_instance_idx == -1:

                if read_only:
                    return None

                if dataset_instances:
                    # Dataset exists but this is a new instance
                    existing_instances = [int(instance.split("_")[1]) for instance in dataset_instances]
                    max_instance_number = max(existing_instances)
                    ds_instance_name = "dataset_" + str(max_instance_number + 1).zfill(3)

                    # Add to metadata dictionary the new instance
                    metadata[ds_name][split][ds_instance_name] = params

                else:
                    # Edge case where, for some error, there was something added to the metadata file but no actual
                    # datasets were recorded. Remove entries from metadata and add them again.
                    ds_instance_name = "dataset_001"
                    metadata[ds_name][split] = {}
                    metadata[ds_name][split][ds_instance_name] = params

            else:
                # Dataset exists and there is an instance with the same configuration
                ds_instance_name = dataset_instances[existing_instance_idx]

        else:
            if read_only:
                return None

            ds_instance_name = "dataset_001"
            safe_mkdir_recursive(os.path.join(rec_file_dir, ds_name, split))

            # Add to metadata dictionary the new instance
            if ds_name in metadata.keys():
                metadata[ds_name][split] = {ds_instance_name: params}
            else:
                metadata[ds_name] = {split: {ds_instance_name: params}}

        if not read_only:
            with open(json_file_name, 'w') as json_file:
                json.dump(metadata, json_file, indent=4)

    return os.path.join(rec_file_dir, ds_name, split), ds_instance_name + '.csv'

def load_pickled_models(directory='', file_name='', model_options=None):
    """
    Loads a pre-trained model from the specified directory, contained in a given pickle filename. Otherwise, if
    the model_options dictionary is given, use its contents to reconstruct the directory location of the pre-trained
    model fitting the requirements.

    :param directory: directory where the model file is located
    :param file_name: file name of the pre-trained model
    :param model_options: dictionary with the keys: "noisy" (bool), "drag" (bool), "git" (string), "training_samples"
    (int), "payload" (bool).

    :return: a dictionary with the recovered models from the pickle files.
    """

    if model_options is not None:
        directory, file_name = get_model_dir_and_file(model_options)

    try:
        pickled_files = os.listdir(directory)
    except FileNotFoundError:
        return None

    loaded_models = []

    try:
        for file in pickled_files:
            if not file.startswith(file_name) and file != 'feats.csv':
                continue
            if '.pkl' not in file and '.csv' not in file:
                continue
            if '.pkl' in file:
                loaded_models.append(joblib.load(os.path.join(directory, file)))

    except IsADirectoryError:
        raise FileNotFoundError("Tried to load file from directory %s, but it was not found." % directory)

    if loaded_models is not None:
        if loaded_models:
            pre_trained_models = {"models": loaded_models}
        else:
            pre_trained_models = None
    else:
        pre_trained_models = None

    return pre_trained_models

def sample_random_points(points, used_idx, points_to_sample, dense_gp=None):
    bins = min(10, int(len(points) / 10))
    bins = max(bins, 2)  #确定直方图 bins 最大10 最小2

    # Add remaining points as random points
    free_points = np.arange(0, points.shape[0], 1)
    gp_i_free_points = np.delete(free_points, used_idx)
    n_samples = min(points_to_sample, len(gp_i_free_points))

    # Compute histogram of data 计算数据分布密度
    # a：直方图计数（形状 (bins, bins, ...)，维度数由 points.shape[1] 决定）。
    # b：分箱边界列表。
    a, b = np.histogramdd(points[gp_i_free_points, :], bins) #bins: 每个维度的分箱数量 a 
    assignments = [np.minimum(np.digitize(points[gp_i_free_points, j], bins=b[j]) - 1, bins - 1)
                   for j in range(points.shape[1])]

    # Compute probability distribution based on inverse histogram 计算采样概率
    probs = np.max(a) - a[tuple(assignments)] #密度越低，概率越高（稀疏区域优先）
    probs = probs / sum(probs) #概率和为 1

    try: #从 gp_i_free_points 中按概率 probs 采样 n_samples 个索引
        gp_i_free_points = np.random.choice(gp_i_free_points, n_samples, p=probs, replace=False)
    except ValueError:
        print('a')
    used_idx = np.append(used_idx, gp_i_free_points)

    return used_idx


def parse_xacro_file(xacro):
    """
    Reads a .xacro file describing a robot for Gazebo and returns a dictionary with its properties.
    :param xacro: full path of .xacro file to read
    :return: a dictionary of robot attributes
    """

    tree = XMLtree.parse(xacro)

    attrib_dict = {}

    for node in tree.getroot().getchildren():
        # Get attributes
        attributes = node.attrib

        if 'value' in attributes.keys():
            attrib_dict[attributes['name']] = attributes['value']

        if node.getchildren():
            try:
                attrib_dict[attributes['name']] = [child.attrib for child in node.getchildren()]
            except:
                continue

    return attrib_dict



def make_bx_matrix(x_dims, y_feats):
    """
    Generates the Bx matrix for the GP augmented MPC.

    :param x_dims: dimensionality of the state vector
    :param y_feats: array with the indices of the state vector x that are augmented by the GP regressor
    :return: The Bx matrix to map the GP output to the state space.
    """

    bx = np.zeros((x_dims, len(y_feats)))
    for i in range(len(y_feats)):
        bx[y_feats[i], i] = 1

    return bx

def make_bz_matrix(x_dims, u_dims, x_feats, u_feats):
    """
    Generates the Bz matrix for the GP augmented MPC.
    :param x_dims: dimensionality of the state vector
    :param u_dims: dimensionality of the input vector
    :param x_feats: array with the indices of the state vector x used to make the first part of the GP feature vector z
    :param u_feats: array with the indices of the input vector u used to make the second part of the GP feature vector z
    :return:  The Bz matrix to map from input x and u features to the z feature vector.
    """

    bz = np.zeros((len(x_feats), x_dims))
    for i in range(len(x_feats)):
        bz[i, x_feats[i]] = 1
    bzu = np.zeros((len(u_feats), u_dims))
    for i in range(len(u_feats)):
        bzu[i, u_feats[i]] = 1
    bz = np.concatenate((bz, np.zeros((len(x_feats), u_dims))), axis=1)
    bzu = np.concatenate((np.zeros((len(u_feats), x_dims)), bzu), axis=1)
    bz = np.concatenate((bz, bzu), axis=0)
    return bz

def separate_variables(traj):
    """
    Reshapes a trajectory into expected format.

    :param traj: N x 13 array representing the reference trajectory
    :return: A list with the components: Nx3 position trajectory array, Nx4 quaternion trajectory array, Nx3 velocity
    trajectory array, Nx3 body rate trajectory array
    """

    p_traj = traj[:, :3]
    a_traj = traj[:, 3:7]
    v_traj = traj[:, 7:10]
    r_traj = traj[:, 10:]
    return [p_traj, a_traj, v_traj, r_traj]

# def quaternion_state_mse(x, x_ref, mask):
#     """
#     Calculates the MSE of the 13-dimensional state (p_xyz, q_wxyz, v_xyz, r_xyz) wrt. the reference state. The MSE of
#     the quaternions are treated axes-wise.

#     :param x: 13-dimensional state
#     :param x_ref: 13-dimensional reference state
#     :param mask: 12-dimensional masking for weighted MSE (p_xyz, q_xyz, v_xyz, r_xyz)
#     :return: the mean squared error of both
#     """

#     q_error = q_dot_q(x[3:7], quaternion_inverse(x_ref[3:7]))
#     e = np.concatenate((x[:3] - x_ref[:3], q_error[1:], x[7:10] - x_ref[7:10], x[10:] - x_ref[10:]))

#     return np.sqrt((e * np.array(mask)).dot(e))


def get_model_dir_and_file(model_options):
    directory = os.path.join(GPConfig.SAVE_DIR, str(model_options["git"]), str(model_options["model_name"]))

    model_params = model_options["params"]
    file_name = ''
    model_vars = list(model_params.keys())
    model_vars.sort()
    for i, param in enumerate(model_vars):
        if i > 0:
            file_name += '__'
        file_name += 'no_' if not model_params[param] else ''  # groove1__no_groove2__no_screw1__no_screw2
        file_name += param

    return directory, file_name


def load_pickled_models(directory='', file_name='', model_options=None):
    """
    Loads a pre-trained model from the specified directory, contained in a given pickle filename. Otherwise, if
    the model_options dictionary is given, use its contents to reconstruct the directory location of the pre-trained
    model fitting the requirements.

    :param directory: directory where the model file is located
    :param file_name: file name of the pre-trained model
    :param model_options: dictionary with the keys: "noisy" (bool), "drag" (bool), "git" (string), "training_samples"
    (int), "payload" (bool).

    :return: a dictionary with the recovered models from the pickle files.
    """

    if model_options is not None:
        directory, file_name = get_model_dir_and_file(model_options)

    try:
        pickled_files = os.listdir(directory)
    except FileNotFoundError:
        return None

    loaded_models = []

    try:
        for file in pickled_files:
            if not file.startswith(file_name) and file != 'feats.csv':
                continue
            if '.pkl' not in file and '.csv' not in file:
                continue
            if '.pkl' in file:
                loaded_models.append(joblib.load(os.path.join(directory, file)))

    except IsADirectoryError:
        raise FileNotFoundError("Tried to load file from directory %s, but it was not found." % directory)

    if loaded_models is not None:
        if loaded_models:
            pre_trained_models = {"models": loaded_models}
        else:
            pre_trained_models = None
    else:
        pre_trained_models = None

    return pre_trained_models


def distance_maximizing_points(x_values, center, n_train_points=7, dense_gp=None, plot=False):
    if x_values.shape[1] == 1:
        return distance_maximizing_points_1d(x_values, n_train_points, dense_gp)  

    if x_values.shape[1] >= 2:
        return distance_maximizing_points_2d(x_values, n_train_points, dense_gp, plot)  #cluster_x_points, cluster_mean, n_train_points=n_train_points, dense_gp=dense_gp, plot=False

    # Compute PCA of data to find variability maximizing axes
    pca = PCA(n_components=3)
    pca.fit(x_values)
    pca_axes = pca.components_
    data_center = center

    # Apply PCA transformation
    points_pca = (x_values - data_center).dot(pca_axes.T)
    center = (center - data_center).dot(pca_axes.T)

    # Compute the corners of the cube containing the data in the PCA space
    p_min = center - (center - np.min(points_pca, 0))
    p_max = (np.max(points_pca, 0) - center) + center

    centroids = np.array([[center[0], center[1], center[2]]])

    pyramids = np.array([[p_max[0], center[1], center[2]], [center[0], p_max[1], center[2]],
                         [center[0], center[1], p_max[2]], [p_min[0], center[1], center[2]],
                         [center[0], p_min[1], center[2]], [center[0], center[1], p_min[2]]])

    cuboid = np.array([[p_max[0], p_max[1], p_max[2]], [p_max[0], p_max[1], p_min[2]],
                       [p_max[0], p_min[1], p_max[2]], [p_max[0], p_min[1], p_min[2]],
                       [p_min[0], p_max[1], p_max[2]], [p_min[0], p_max[1], p_min[2]],
                       [p_min[0], p_min[1], p_max[2]], [p_min[0], p_min[1], p_min[2]]])

    if n_train_points >= 15:
        centroids = np.concatenate((centroids, pyramids, cuboid), axis=0)
    elif n_train_points >= 9:
        centroids = np.concatenate((centroids, cuboid), axis=0)
    elif n_train_points >= 7:
        centroids = np.concatenate((centroids, pyramids), axis=0)
    else:
        centroids = centroids

    if dense_gp is None:

        closest_points = np.ones(centroids.shape[0], dtype=int) * -1

        # Find the closest points to all centroids
        for i in range(centroids.shape[0]):
            centroid = centroids[i, :]
            dist = np.sqrt(np.sum((points_pca - centroid) ** 2, 1))
            closest_point = int(np.argmin(dist))

            # Assert no repeated points. If repeated, find next closest one and check again
            while closest_point in closest_points:
                dist[closest_point] = np.inf
                closest_point = int(np.argmin(dist))
            closest_points[i] = closest_point

        # Convert centroids to data space
        centroids_ = centroids.dot(pca_axes) + data_center

        if not plot:
            return closest_points

        fig = plt.figure()

        ax = fig.add_subplot(122, projection='3d')
        ax.scatter(points_pca[:, 0], points_pca[:, 1], points_pca[:, 2], 'b', label='data')

        ax.scatter(centroids[0, 0], centroids[0, 1], centroids[0, 2], s=50, label='center')
        ax.scatter(centroids[1:, 0], centroids[1:, 1], centroids[1:, 2], s=50, label='centroids')
        ax.scatter(points_pca[closest_points, 0], points_pca[closest_points, 1], points_pca[closest_points, 2],
                   s=50, label='selected')
        ax.set_title('PCA space')
        ax.legend()

        ax = fig.add_subplot(121, projection='3d')
        ax.scatter(x_values[:, 0], x_values[:, 1], x_values[:, 2], 'b', label='data')

        closest_points_x = x_values[closest_points]
        ax.scatter(centroids_[0, 0], centroids_[0, 1], centroids_[0, 2], s=50, label='center')
        ax.scatter(centroids_[1:, 0], centroids_[1:, 1], centroids_[1:, 2], s=50, label='centroids')
        ax.scatter(closest_points_x[:, 0], closest_points_x[:, 1], closest_points_x[:, 2], s=50, label='selected')
        ax.set_title('Data space')
        ax.legend()
        plt.show()

        # Returns the indices of the closest points from the dataset to the ideal ones
        return closest_points

    else:

        # TODO: Use GP covariance for sampling
        # Convert centroids to data space
        centroids_ = centroids.dot(pca_axes) + data_center

        return centroids_.T


def distance_maximizing_points_1d(points, n_train_points, dense_gp=None):
    """
    Heuristic function for sampling training points in 1D (one input feature and one output prediction dimensions)
    :param points: dataset points for the current cluster. Array of shape Nx1
    :param n_train_points: Integer. number of training points to sample.
    :param dense_gp: A GP object to sample the points from, or None of the points will be taken directly from the data.
    :return:
    """

    closest_points = np.zeros(n_train_points, dtype=int if dense_gp is None else float)

    if dense_gp is not None:
        n_train_points -= 1

    # Fit histogram in data with as many bins as the number of training points
    a, b = np.histogram(points, bins=n_train_points)
    hist_indices = np.digitize(points, b) - 1

    # Pick as training value the median or mean value of each bin
    for i in range(n_train_points):
        bin_values = points[np.where(hist_indices == i)]
        if len(bin_values) < 1:
            closest_points[i] = np.random.choice(np.arange(len(points)), 1)
            continue
        if divmod(len(bin_values), 2)[1] == 0:
            bin_values = bin_values[:-1]

        if dense_gp is None:
            # If no dense GP, sample median points in each bin from training set
            bin_median = np.median(bin_values)
            median_point_id = np.where(points == bin_median)[0]
            if len(median_point_id) > 1:
                closest_points[i] = median_point_id[0]
            else:
                closest_points[i] = median_point_id
        else:
            # If with GP, sample mean points in each bin from GP
            bin_mean = np.min(bin_values)
            closest_points[i] = bin_mean

    if dense_gp is not None:
        # Add dimension axis 0
        closest_points[-1] = np.max(points)
        closest_points = closest_points[np.newaxis, :]

    return closest_points

def distance_maximizing_points_2d(points, n_train_points, dense_gp, plot=False):
    #从输入数据 points 中选择 n_train_points 个分散的点
    #使用 KMeans 聚类分割数据，从每个簇随机采样点，确保分布均匀
    if n_train_points > 30:
        n_clusters = max(int(n_train_points / 10), 30) #簇数取 1/10 或至少 30，确保分布广泛；采样数分配均匀
        n_samples = int(np.floor(n_train_points / n_clusters)) #每个簇的样本数量
    else:
        n_clusters = n_train_points
        n_samples = 1

    kmeans = KMeans(n_clusters).fit_predict(points) 
    #使用 KMeans 将 points 分为 n_clusters 个簇
    #fit_predict 返回每个样本的簇标签

    closest_points = []
    for i in range(n_clusters): #从每个簇采样点
        closest_points += np.random.choice(np.where(kmeans == i)[0], n_samples).tolist()
    # 遍历每个簇，从中随机采样 n_samples 个点索引，追加到 closest_points 列表

    # Remove exceeding points 若采样点数超过 n_train_points，随机移除多余点
    for _ in range(len(closest_points) - n_train_points):
        rnd_item = random.choice(closest_points)
        closest_points.remove(rnd_item)
    closest_points = np.array(closest_points)

    if plot:
        plt.figure()
        for i in range(n_clusters):
            cluster_points = points[np.where(kmeans == i)]
            plt.scatter(cluster_points[:, 0], cluster_points[:, 1])
        plt.scatter(points[closest_points, 0], points[closest_points, 1], marker='*', facecolors='w',
                    edgecolors='k', s=100, label='selected')
        plt.legend()
        plt.show()

    if dense_gp is None:
        return closest_points

    closest_points = points[closest_points].T
    return closest_points


def prune_dataset(x, y, x_cap, bins, thresh, plot, labels=None):
    """
    prune_dataset 是一个独立的函数，用于对数据集应用两种筛选规则，返回保留的数据索引。它还支持可视化清洗过程
    Prunes the collected model error dataset with two filters. First, remove values where the input values (velocities)
    exceed 10. Second, create an histogram for each of the three axial velocity errors (y) with the specified number of
    bins and remove any data where the total amount of samples in that bin is less than the specified threshold ratio.
    :param x: dataset of input GP features (velocities). Dimensions N x n (N entries and n dimensions)
    :param y: dataset of errors. Dimensions N x m (N entries and m dimensions)
    :param x_cap: remove values from dataset if x > x_cap or x < -x_cap
    :param bins: number of bins used for histogram
    :param thresh: threshold ratio below which data from that bin will be removed
    :param plot: make a plot of the pruning
    :param labels: Labels to use for the plot
    :return: The indices kept after the pruning
    x：输入特征数据集（例如速度），形状为 N x n（N 个样本，n 个维度）。
    y：误差数据集，形状为 N x m（N 个样本，m 个维度）。
    x_cap：输入值的上限，用于移除超出范围的数据。
    bins：直方图的分箱数。
    thresh：阈值比例，用于移除样本数过少的直方图区间。
    plot：布尔值，是否绘制清洗过程的直方图。
    labels：可选的标签，用于绘图。
    """

    n_bins = bins
    original_length = x.shape[0] #记录原始样本数量

    plot_bins = []
    if plot:
        plt.figure()
        for i in range(y.shape[1]):
            plt.subplot(y.shape[1] + 1, 1, i + 1)
            h, bins = np.histogram(y[:, i], bins=n_bins)
            plot_bins.append(bins)
            plt.bar(bins[:-1], h, np.ones_like(h) * (bins[1] - bins[0]), align='edge', label='discarded')
            if labels is not None:
                plt.ylabel(labels[i])

    pruned_idx_unique = np.zeros(0, dtype=int)

    # Prune velocities (max axial velocity = x_cap m/s).  第一次筛选，基于输入值x的上限
    if x_cap is not None:
        for i in range(x.shape[1]):
            pruned_idx = np.where(np.abs(x[:, i]) > x_cap)[0]  #对 x 的每个维度（列），检查是否超出范围（abs(x[:, i]) > x_cap）
            pruned_idx_unique = np.unique(np.append(pruned_idx, pruned_idx_unique)) #收集所有需要移除的唯一索引

    # Prune by error histogram dimension wise (discard bins with less than 1% of the data) 第二次筛选：基于误差（y）的直方图分布
    for i in range(y.shape[1]):
        """
        np.histogram(y[:, i], bins=n_bins)：计算直方图，返回频率 h 和分箱边界 bins。
        检查每个分箱的样本比例 h[j] / np.sum(h) 是否低于 thresh。
        如果低于阈值，找到该分箱范围内的样本索引（bins[j] <= y[:, i] <= bins[j+1]），加入 pruned_idx_unique。
        """
        h, bins = np.histogram(y[:, i], bins=n_bins)
        for j in range(len(h)):
            if h[j] / np.sum(h) < thresh:
                pruned_idx = np.where(np.logical_and(bins[j + 1] >= y[:, i], y[:, i] >= bins[j]))
                pruned_idx_unique = np.unique(np.append(pruned_idx, pruned_idx_unique))

    y_norm = np.sqrt(np.sum(y ** 2, 1))

    # Prune by error histogram norm 第三次筛选：基于误差范数（y_norm）的直方图
    h, error_bins = np.histogram(y_norm, bins=n_bins)
    h = h / np.sum(h)
    if plot:
        plt.subplot(y.shape[1] + 1, 1, y.shape[1] + 1)
        plt.bar(error_bins[:-1], h, np.ones_like(h) * (error_bins[1] - error_bins[0]), align='edge', label='discarded')

    for j in range(len(h)):
        if h[j] / np.sum(h) < thresh:
            pruned_idx = np.where(np.logical_and(error_bins[j + 1] >= y_norm, y_norm >= error_bins[j]))
            pruned_idx_unique = np.unique(np.append(pruned_idx, pruned_idx_unique))

    y = np.delete(y, pruned_idx_unique, axis=0) #移除数据并更新绘图

    if plot:
        for i in range(y.shape[1]):
            plt.subplot(y.shape[1] + 1, 1, i + 1)
            h, bins = np.histogram(y[:, i], bins=plot_bins[i])
            plt.bar(bins[:-1], h, np.ones_like(h) * (bins[1] - bins[0]), align='edge', label='kept')
            plt.legend()

        plt.subplot(y.shape[1] + 1, 1, y.shape[1] + 1)
        h, bins = np.histogram(np.sqrt(np.sum(y ** 2, 1)), bins=error_bins)
        h = h / sum(h)
        plt.bar(bins[:-1], h, np.ones_like(h) * (bins[1] - bins[0]), align='edge', label='kept')
        plt.ylabel('Error norm')

    kept_idx = np.delete(np.arange(0, original_length), pruned_idx_unique)
    return kept_idx


def q_dot_q(q, r):
    """
    Applies the rotation of quaternion r to quaternion q. In order words, rotates quaternion q by r. Quaternion format:
    wxyz.

    :param q: 4-length numpy array or CasADi MX. Initial rotation
    :param r: 4-length numpy array or CasADi MX. Applied rotation
    :return: The quaternion q rotated by r, with the same format as in the input.
    """

    qw, qx, qy, qz = q[0], q[1], q[2], q[3]
    rw, rx, ry, rz = r[0], r[1], r[2], r[3]

    t0 = rw * qw - rx * qx - ry * qy - rz * qz
    t1 = rw * qx + rx * qw - ry * qz + rz * qy
    t2 = rw * qy + rx * qz + ry * qw - rz * qx
    t3 = rw * qz - rx * qy + ry * qx + rz * qw

    if isinstance(q, np.ndarray):
        return np.array([t0, t1, t2, t3])
    else:
        return cs.vertcat(t0, t1, t2, t3)

def quaternion_inverse(q):
    w, x, y, z = q[0], q[1], q[2], q[3]

    if isinstance(q, np.ndarray):
        return np.array([w, -x, -y, -z])
    else:
        return cs.vertcat(w, -x, -y, -z)

def q_to_rot_mat(q): #四元数->旋转矩阵
    qw, qx, qy, qz = q[0], q[1], q[2], q[3]

    if isinstance(q, np.ndarray):
        rot_mat = np.array([
            [1 - 2 * (qy ** 2 + qz ** 2), 2 * (qx * qy - qw * qz), 2 * (qx * qz + qw * qy)],
            [2 * (qx * qy + qw * qz), 1 - 2 * (qx ** 2 + qz ** 2), 2 * (qy * qz - qw * qx)],
            [2 * (qx * qz - qw * qy), 2 * (qy * qz + qw * qx), 1 - 2 * (qx ** 2 + qy ** 2)]])

    else:
        rot_mat = cs.vertcat(
            cs.horzcat(1 - 2 * (qy ** 2 + qz ** 2), 2 * (qx * qy - qw * qz), 2 * (qx * qz + qw * qy)),
            cs.horzcat(2 * (qx * qy + qw * qz), 1 - 2 * (qx ** 2 + qz ** 2), 2 * (qy * qz - qw * qx)),
            cs.horzcat(2 * (qx * qz - qw * qy), 2 * (qy * qz + qw * qx), 1 - 2 * (qx ** 2 + qy ** 2)))

    return rot_mat

def v_dot_q(v, q): #矩阵*向量
    rot_mat = q_to_rot_mat(q)
    if isinstance(q, np.ndarray):
        return rot_mat.dot(v)

    return cs.mtimes(rot_mat, v)

def quaternion_state_mse(x, x_ref, mask):
    """
    Calculates the MSE of the 13-dimensional state (p_xyz, q_wxyz, v_xyz, r_xyz) wrt. the reference state. The MSE of
    the quaternions are treated axes-wise.

    :param x: 13-dimensional state
    :param x_ref: 13-dimensional reference state
    :param mask: 12-dimensional masking for weighted MSE (p_xyz, q_xyz, v_xyz, r_xyz)
    :return: the mean squared error of both
    """

    q_error = q_dot_q(x[3:7], quaternion_inverse(x_ref[3:7]))
    e = np.concatenate((x[:3] - x_ref[:3], q_error[1:], x[7:10] - x_ref[7:10], x[10:] - x_ref[10:]))

    return np.sqrt((e * np.array(mask)).dot(e))

def quaternion_to_euler(q):
    q = pyquaternion.Quaternion(w=q[0], x=q[1], y=q[2], z=q[3])
    yaw, pitch, roll = q.yaw_pitch_roll
    return [roll, pitch, yaw]