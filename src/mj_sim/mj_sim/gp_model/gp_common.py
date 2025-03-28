""" Contains a set of utility functions and classes for the GP training and inference.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""


import copy
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import joblib
import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture

from gp import GPEnsemble, CustomGPRegression as npGPRegression
from utils import undo_jsonify, prune_dataset, safe_mknode_recursive, get_data_dir_and_file, \
    separate_variables
from visualization import visualize_data_distribution

# 改写这个类，获取我需要的状态
class GPDataset:
    def __init__(self, raw_ds=None,
                 x_features=None, u_features=None, y_dim=None,
                 cap=None, n_bins=None, thresh=None,
                 visualize_data=False):

        self.data_labels = [r'$\delta_x$', r'$\delta_x_dot$', r'$\delta_fx$', 
                            r'$\delta_y$', r'$\delta_y_dot$', r'$\delta_fy$',
                            r'$\delta_z$', r'$\delta_z_dot$', r'$\delta_fz$']

        # Raw dataset data
        self.x_raw = None
        self.x_out_raw = None
        self.u_raw = None
        self.y_raw = None
        self.x_pred_raw = None
        self.dt_raw = None

        self.x_ref = None
        self.x_error = None

        self.x_features = x_features
        self.u_features = u_features
        self.y_dim = y_dim

        # Data pruning parameters
        self.cap = cap
        self.n_bins = n_bins
        self.thresh = thresh
        self.plot = visualize_data

        # GMM clustering
        self.pruned_idx = []
        self.cluster_agency = None
        self.centroids = None

        # Number of data clusters
        self.n_clusters = 1

        if raw_ds is not None:
            self.load_data(raw_ds)
            self.prune()

    def load_data(self, ds):
        # x_raw = undo_jsonify(ds['state_in'].to_numpy())  # 二维数组
        # x_out = undo_jsonify(ds['state_out'].to_numpy())
        # x_pred = undo_jsonify(ds['state_pred'].to_numpy())
        # u_raw = undo_jsonify(ds['input_in'].to_numpy())

        """
        "state_in_pose": np.zeros((0, 3+9)),    # 位置+旋转矩阵，第一步初始状态
        "state_in_vel": np.zeros((0, 6)),       # 速度
        "state_in_force": np.zeros((0, 6)),     # 力/力矩
        "state_ref_pose": np.zeros((0, 7)),     # 位置+四元数
        "state_ref_vel": np.zeros((0, 6)),      # 6维度速度
        "error": np.zeros((0, 3*3)),            # 3 * (x-x_r, x_dot-x_dot_r, f-f_r) 实际状态（state_out）与预测状态（state_pred）之间的误差
        "input_in": np.zeros((0, 6+6)),         # (k,d)*6维，当前状态情况下的输入
        "state_pred": np.zeros((0, 3*3)),       # 基于理论动力学模型预测的状态， 3 * (x, x_dot, f)
        "timestamp": np.zeros((0, 1)),          # 时间戳
        """

        x_raw = undo_jsonify(ds['state_in_pose'].to_numpy())  #当前状态
        x_ref = undo_jsonify(ds['state_ref_pose'].to_numpy()) #当前参考状态
        x_pred = undo_jsonify(ds['state_pred'].to_numpy())    #当前对下一时刻的预测状态 3 * (x, x_dot, f)
        x_error = undo_jsonify(ds['error'].to_numpy())        #当强状态误差 3 * (x-x_r, x_dot-x_dot_r, f-f_r)
        u_raw = undo_jsonify(ds['input_in'].to_numpy())       #当前控制输入
        x_out = undo_jsonify(ds['state_out'].to_numpy())       #下一时刻真实状态

        # dt = ds["dt"].to_numpy()
        # invalid = np.where(dt == 0)

        # # Remove invalid entries (dt = 0)
        # x_raw = np.delete(x_raw, invalid, axis=0)
        # x_out = np.delete(x_out, invalid, axis=0)
        # x_pred = np.delete(x_pred, invalid, axis=0)
        # u_raw = np.delete(u_raw, invalid, axis=0)
        # dt = np.delete(dt, invalid, axis=0)

        # Rotate velocities to body frame and recompute errors
        # x_raw = world_to_body_velocity_mapping(x_raw)
        # x_pred = world_to_body_velocity_mapping(x_pred)
        # x_out = world_to_body_velocity_mapping(x_out)
        y_err = x_out[:, :3] - x_pred[:, [2,5,8]] # x y z 维度的力

        # Normalize error by window time (i.e. predict error dynamics instead of error itself)
        # y_err /= np.expand_dims(dt, 1)

        # Select features
        self.x_raw = x_raw
        self.x_ref = x_ref
        self.x_pred_raw = x_pred
        self.x_error = x_error
        self.u_raw = u_raw
        self.y_raw = y_err  #下一时刻力的真实值-预测值，用于训练的目标

    def prune(self):
        # Prune noisy data
        if self.cap is not None and self.n_bins is not None and self.thresh is not None:
            x_interest = np.array([2, 5, 8])
            y_interest = np.array([0, 1, 2])

            labels = [self.data_labels[dim] for dim in np.atleast_1d(x_interest)] #提取标签的名称  np.atleast_1d(y_interest) 确保y_interest至少是一维以上的数组

            prune_x_data = self.get_x(pruned=False, raw=True)[:, x_interest] #这行没有变换数据，也可以改变参数，添加u维度
            prune_y_data = self.get_y(pruned=False, raw=True)[:, y_interest]
            # self.pruned_idx.append(prune_dataset(prune_x_data, prune_y_data, self.cap, self.n_bins, self.thresh,
            #                                      plot=self.plot, labels=labels))  #数据清洗并存储
            #prune_dataset 返回保留的数据索引，追加到 self.pruned_idx（一个列表，用于跟踪清洗后的数据索引）。
            #规则 1：移除输入值（x）绝对值超过 x_cap 的样本（例如速度超过 10 m/s）。
            #规则 2：对每个误差维度（y）和误差范数创建直方图，移除样本比例低于 thresh 的分箱中的数据（例如移除少于 1% 的稀疏数据）。

    def get_x(self, cluster=None, pruned=True, raw=False):

        if cluster is not None: #确保在处理聚类数据时，数据已经被剪枝（pruned）
            assert pruned #断言 pruned 必须为 True

        if raw:
            return self.x_raw[tuple(self.pruned_idx)] if pruned else self.x_raw #Python 的内置函数，将输入转换为元组（tuple）类型。例如：tuple([0, 2]) → (0, 2)。

        if self.x_features is not None and self.u_features is not None:
            x_f = self.x_features
            u_f = self.u_features
            data = np.concatenate((self.x_raw[:, x_f], self.u_raw[:, u_f]), axis=1) if u_f else self.x_raw[:, x_f]
            # print(data)
        else:
            data = np.concatenate((self.x_raw, self.u_raw), axis=1)
        data = data[:, np.newaxis] if len(data.shape) == 1 else data #保证数据是二维的

        if pruned or cluster is not None: #pruned 必须是 True，或者 cluster 必须不是 None，条件才会成立
            data = data[tuple(self.pruned_idx)]
            data = data[self.cluster_agency[cluster]] if cluster is not None else data

        return data

    @property
    def x(self):
        return self.get_x()
    

    def get_x_error(self, cluster=None, pruned=True, raw=False):

        if cluster is not None: #确保在处理聚类数据时，数据已经被剪枝（pruned）
            assert pruned #断言 pruned 必须为 True

        if raw:
            return self.x_error[tuple(self.pruned_idx)] if pruned else self.x_error #Python 的内置函数，将输入转换为元组（tuple）类型。例如：tuple([0, 2]) → (0, 2)。

        if self.x_features is not None and self.u_features is not None:
            x_f = self.x_features
            u_f = self.u_features
            data = np.concatenate((self.x_error[:, x_f], self.u_raw[:, u_f]), axis=1) if u_f else self.x_error[:, x_f]
            # print(data.shape)
        else:
            data = np.concatenate((self.x_error, self.u_raw), axis=1)
        data = data[:, np.newaxis] if len(data.shape) == 1 else data #保证数据是二维的

        if pruned or cluster is not None: #pruned 必须是 True，或者 cluster 必须不是 None，条件才会成立
            data = data[tuple(self.pruned_idx)]
            data = data[self.cluster_agency[cluster]] if cluster is not None else data

        # print(data.shape)
        return data

    @property
    def x_err(self):
        return self.get_x_error()

    def get_x_out(self, cluster=None, pruned=True):

        if cluster is not None:
            assert pruned

        if pruned or cluster is not None:
            data = self.x_out_raw[tuple(self.pruned_idx)]
            data = data[self.cluster_agency[cluster]] if cluster is not None else data

            return data

        return self.x_out_raw[tuple(self.pruned_idx)] if pruned else self.x_out_raw

    @property
    def x_out(self):
        return self.get_x_out()

    def get_u(self, cluster=None, pruned=True, raw=False):

        if cluster is not None:
            assert pruned

        if raw:
            return self.u_raw[tuple(self.pruned_idx)] if pruned else self.u_raw

        data = self.u_raw[:, self.u_features] if self.u_features is not None else self.u_raw
        data = data[:, np.newaxis] if len(data.shape) == 1 else data

        if pruned or cluster is not None:
            data = data[tuple(self.pruned_idx)]
            data = data[self.cluster_agency[cluster]] if cluster is not None else data

        return data

    @property
    def u(self):
        return self.get_u()

    def get_y(self, cluster=None, pruned=True, raw=False):

        if cluster is not None:
            assert pruned

        if raw:
            return self.y_raw[self.pruned_idx] if pruned else self.y_raw

        data = self.y_raw[:, self.y_dim] if self.y_dim is not None else self.y_raw
        data = data[:, np.newaxis] if len(data.shape) == 1 else data

        if pruned or cluster is not None:
            data = data[tuple(self.pruned_idx)]
            data = data[self.cluster_agency[cluster]] if cluster is not None else data

        return data

    @property
    def y(self):
        return self.get_y()

    def get_x_pred(self, pruned=True, raw=False):

        if raw:
            return self.x_pred_raw[tuple(self.pruned_idx)] if pruned else self.x_pred_raw

        data = self.x_pred_raw[:, self.y_dim] if self.y_dim is not None else self.x_pred_raw
        data = data[:, np.newaxis] if len(data.shape) == 1 else data

        if pruned:
            data = data[tuple(self.pruned_idx)]

        return data

    @property
    def x_pred(self):
        return self.get_x_pred()

    def get_dt(self, pruned=True):

        return self.dt_raw[tuple(self.pruned_idx)] if pruned else self.dt_raw

    @property
    def dt(self):
        return self.get_dt()

    def cluster(self, n_clusters, load_clusters=False, save_dir="", visualize_data=False):
        """
        使用高斯混合模型（Gaussian Mixture Model, GMM）对数据进行聚类，将数据集分为 n_clusters 个簇。
        为每个簇分配数据点，并计算簇质心（centroids），支持后续 GP 集成模型（如 GPEnsemble）的使用。
        """
        self.n_clusters = n_clusters

        x_pruned = self.x_err
        y_pruned = self.y
        # print(x_pruned)
        # print(x_pruned.shape)
        # print(y_pruned.shape)

        file_name = os.path.join(save_dir, 'gmm.pkl')
        loaded = False
        gmm = None
        if os.path.exists(file_name) and load_clusters:
            print("Loaded GP clusters from last GP training session. File: {}".format(file_name))
            gmm = joblib.load(file_name)
            if gmm.n_components != n_clusters:
                print("The loaded GP does not coincide with the number of set clusters: Found {} but requested"
                      "is {}".format(gmm.n_components, n_clusters))
            else:
                loaded = True
        if not loaded: #若未加载（loaded=False），用 GaussianMixture(n_clusters) 在 x_pruned 上训练 GMM
            gmm = GaussianMixture(n_clusters).fit(x_pruned)
            # print(gmm)
        clusters = gmm.predict_proba(x_pruned)
        # 返回概率矩阵，形状为 (n_samples, n_clusters)，每行是样本属于各簇的概率
        centroids = gmm.means_
        # 回质心数组，形状为 (n_clusters, n_features)，每个簇的中心

        #means_ 是每个簇的中心，用于 GPEnsemble 的模型选择

        if not load_clusters and n_clusters > 1:
            safe_mknode_recursive(save_dir, 'gmm.pkl', overwrite=True)  #创建空文件
            joblib.dump(gmm, file_name) #创建保存目录并保存 GMM 模型到 gmm.pkl

        index_aux = np.arange(0, clusters.shape[0])
        cluster_agency = {}

        # Add to the points corresponding to each cluster the points that correspond to it with top 2 probability,
        # if this probability is high
        for cluster in range(n_clusters):
            top_1 = np.argmax(clusters, 1) #属于哪个簇的局部索引
            clusters_ = copy.deepcopy(clusters)
            clusters_[index_aux, top_1] *= 0
            top_2 = np.argmax(clusters_, 1)
            idx = np.where(top_1 == cluster)[0]
            idx = np.append(idx, np.where((top_2 == cluster) * (clusters_[index_aux, top_2] > 0.2))[0]) #将 top_2 为当前簇且概率大于 0.2 的样本索引追加到 idx
            cluster_agency[cluster] = idx #：cluster_agency[cluster] = idx，每个簇的样本索引集合

        # Only works in len(x_features) >= 3
        if visualize_data:
            x_aux = self.get_x_error(pruned=False)
            y_aux = self.get_y(pruned=False)
            visualize_data_distribution(x_aux, y_aux, cluster_agency, x_pruned, y_pruned)

        self.cluster_agency = cluster_agency
        self.centroids = centroids   

        # print(self.cluster_agency)
        # print(self.centroids)

        # self.cluster_agency：每个簇的样本索引字典。
        # self.centroids：簇质心数组。


def restore_gp_regressors(pre_trained_models):
    """
    :param pre_trained_models: A dictionary with all the GP models to be restored in 'models'.
    :return: The GP ensemble restored from the models.
    :rtype: GPEnsemble
    """

    gp_reg_ensemble = GPEnsemble()
    # TODO: Deprecate compatibility mode with old models.
    if all(item in list(pre_trained_models.keys()) for item in ["x_features", "u_features"]):
        x_features = pre_trained_models["x_features"]
        u_features = pre_trained_models["u_features"]
    else:
        x_features = u_features = None

    if isinstance(pre_trained_models['models'][0], dict):
        pre_trained_gp_reg = {}
        for _, model_dict in enumerate(pre_trained_models['models']):
            if x_features is not None:
                gp_reg = npGPRegression(x_features, u_features, model_dict["reg_dim"])
            else:
                gp_reg = npGPRegression(model_dict["x_features"], model_dict["u_features"], model_dict["reg_dim"])
            gp_reg.load(model_dict)
            if model_dict["reg_dim"] not in pre_trained_gp_reg.keys():
                pre_trained_gp_reg[model_dict["reg_dim"]] = [gp_reg]
            else:
                pre_trained_gp_reg[model_dict["reg_dim"]] += [gp_reg]

        # Add the GP's in a per-output-dim basis into the Ensemble
        for key in np.sort(list(pre_trained_gp_reg.keys())):
            gp_reg_ensemble.add_model(pre_trained_gp_reg[key])
    else:
        raise NotImplementedError("Cannot load this format of GP model.")

    return gp_reg_ensemble


def read_dataset(name, train_split, sim_options):
    """
    Attempts to read a dataset given its name and its metadata.
    :param name: Name of the dataset
    :param train_split: Whether to load the training split (True) or the test split (False)
    :param sim_options: Dictionary of metadata of the dataset to be read.
    :return:
    """
    data_file = get_data_dir_and_file(name, training_split=train_split, params=sim_options, read_only=True)
    if data_file is None:
        raise FileNotFoundError
    rec_file_dir, rec_file_name = data_file
    rec_file = os.path.join(rec_file_dir, rec_file_name)
    ds = pd.read_csv(rec_file)

    return ds


# def world_to_body_velocity_mapping(state_sequence):
#     """

#     :param state_sequence: N x 13 state array, where N is the number of states in the sequence.
#     :return: An N x 13 sequence of states, but where the velocities (assumed to be in positions 7, 8, 9) have been
#     rotated from world to body frame. The rotation is made using the quaternion in positions 3, 4, 5, 6.
#     """

#     p, q, v_w, w = separate_variables(state_sequence)
#     v_b = []
#     for i in range(len(q)):
#         v_b.append(v_dot_q(v_w[i], quaternion_inverse(q[i])))
#     v_b = np.stack(v_b)
#     return np.concatenate((p, q, v_b, w), 1)