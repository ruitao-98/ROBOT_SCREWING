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

def safe_mkdir_recursive(directory, overwrite=False):
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

# def safe_mknode_recursive(destiny_dir, node_name, overwrite):
#     safe_mkdir_recursive(destiny_dir)
#     if overwrite and os.path.exists(os.path.join(destiny_dir, node_name)):
#         os.remove(os.path.join(destiny_dir, node_name))
#     if not os.path.exists(os.path.join(destiny_dir, node_name)):
#         os.mknod(os.path.join(destiny_dir, node_name))
#         return False
#     return True

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
    bins = max(bins, 2)

    # Add remaining points as random points
    free_points = np.arange(0, points.shape[0], 1)
    gp_i_free_points = np.delete(free_points, used_idx)
    n_samples = min(points_to_sample, len(gp_i_free_points))

    # Compute histogram of data
    a, b = np.histogramdd(points[gp_i_free_points, :], bins)
    assignments = [np.minimum(np.digitize(points[gp_i_free_points, j], bins=b[j]) - 1, bins - 1)
                   for j in range(points.shape[1])]

    # Compute probability distribution based on inverse histogram
    probs = np.max(a) - a[tuple(assignments)]
    probs = probs / sum(probs)

    try:
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


# def get_model_dir_and_file(model_options):
#     directory = os.path.join(GPConfig.SAVE_DIR, str(model_options["git"]), str(model_options["model_name"]))

#     model_params = model_options["params"]
#     file_name = ''
#     model_vars = list(model_params.keys())
#     model_vars.sort()
#     for i, param in enumerate(model_vars):
#         if i > 0:
#             file_name += '__'
#         file_name += 'no_' if not model_params[param] else ''
#         file_name += param

#     return directory, file_name


# def load_pickled_models(directory='', file_name='', model_options=None):
#     """
#     Loads a pre-trained model from the specified directory, contained in a given pickle filename. Otherwise, if
#     the model_options dictionary is given, use its contents to reconstruct the directory location of the pre-trained
#     model fitting the requirements.

#     :param directory: directory where the model file is located
#     :param file_name: file name of the pre-trained model
#     :param model_options: dictionary with the keys: "noisy" (bool), "drag" (bool), "git" (string), "training_samples"
#     (int), "payload" (bool).

#     :return: a dictionary with the recovered models from the pickle files.
#     """

#     if model_options is not None:
#         directory, file_name = get_model_dir_and_file(model_options)

#     try:
#         pickled_files = os.listdir(directory)
#     except FileNotFoundError:
#         return None

#     loaded_models = []

#     try:
#         for file in pickled_files:
#             if not file.startswith(file_name) and file != 'feats.csv':
#                 continue
#             if '.pkl' not in file and '.csv' not in file:
#                 continue
#             if '.pkl' in file:
#                 loaded_models.append(joblib.load(os.path.join(directory, file)))

#     except IsADirectoryError:
#         raise FileNotFoundError("Tried to load file from directory %s, but it was not found." % directory)

#     if loaded_models is not None:
#         if loaded_models:
#             pre_trained_models = {"models": loaded_models}
#         else:
#             pre_trained_models = None
#     else:
#         pre_trained_models = None

#     return pre_trained_models