# import numpy as np


# eef_rotm = np.zeros((3,3))
# eef_pos = np.zeros(3)
# eef_pos1 = eef_pos.copy()
# eef_pos1[1] = 2
# eef_pos2 = eef_pos + eef_pos1

# print(eef_pos)
# print(eef_rotm)

# print (eef_pos2 + eef_rotm@eef_pos)

# print(np.eye(3))

# from scipy.spatial.transform import Rotation as R
# import numpy as np

# # 定义绕 x 轴旋转 90 度（角度单位为度）
# rot = R.from_euler('x', 90, degrees=True)

# # 获取旋转矩阵
# rotation_matrix = rot.as_matrix()

# # 打印结果
# print("绕 x 轴旋转 90 度的旋转矩阵：")
# print(rotation_matrix)
# print(type(rotation_matrix))



# import numpy as np
# arr = np.zeros((100, 3))  # 模拟 self.x_ref，形状 (100, 3)
# slice_result = arr[95:145, :]  # 切片超出范围
# print(slice_result.shape)  # 输出: (5, 3)
# print(slice_result)  # 输出从索引 95 到 99 的行

# import os

# class DirectoryConfig:
#     """
#     Class for storing directories within the package
#     """

#     _dir_path = os.path.dirname(os.path.realpath(__file__))
#     SAVE_DIR = _dir_path + '/../results/model_fitting'
#     RESULTS_DIR = _dir_path + '/../results'
#     CONFIG_DIR = _dir_path + ''
#     DATA_DIR = _dir_path + '/../data'


# print(DirectoryConfig.DATA_DIR)

# print(np.zeros((0, 12)))

from tqdm import tqdm
import time

n_clusters = 5

range_vec = tqdm(range(n_clusters))  #range_vec 是一个 tqdm 迭代器对象，可以像普通 range 一样用于 for 循环，但会显示进度条

# print(range_vec)

for cluster in range_vec:
    time.sleep(1)
    range_vec.set_description(f"Cluster")
    # tqdm.write(f"X shape: {cluster}")
    range_vec.set_postfix({
        'X': str(cluster),
    })



import numpy as np

class Test:
    def __init__(self):
        self.u_raw = np.array([[1, 2, 3], [4, 5, 6]])  # shape: (2, 3)
        self.u_features = []  # 空数组

    def get_data(self):
        data = self.u_raw[:, self.u_features] if self.u_features is not None else self.u_raw
        data = data[:, np.newaxis] if len(data.shape) == 1 else data
        return data

test = Test()
result = test.get_data()
print(result.shape)  # 输出: (2, 0)
print(result)       # 输出: array([], shape=(2, 0), dtype=int64)