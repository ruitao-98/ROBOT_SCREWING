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




# import numpy as np

# def gaussian_kernel(x1, x2, l=1.0, sigma_f=1.0):
#     """Easy to understand but inefficient."""
#     m, n = x1.shape[0], x2.shape[0]
#     dist_matrix = np.zeros((m, n), dtype=float)
#     for i in range(m):
#         for j in range(n):
#             dist_matrix[i][j] = np.sum((x1[i] - x2[j]) ** 2)
#     return sigma_f ** 2 * np.exp(- 0.5 / l ** 2 * dist_matrix)

# def gaussian_kernel_vectorization(x1, x2, l=1.0, sigma_f=1.0):
#     """More efficient approach."""
#     dist_matrix = np.sum(x1**2, 1).reshape(-1, 1) + np.sum(x2**2, 1) - 2 * np.dot(x1, x2.T)
#     return sigma_f ** 2 * np.exp(-0.5 / l ** 2 * dist_matrix)

# x = np.array([700, 800, 1029]).reshape(-1, 1)
# print(gaussian_kernel_vectorization(x, x, l=500, sigma_f=10))

# from scipy.optimize import minimize
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# class GPR:

#     def __init__(self, optimize=True):
#         self.is_fit = False
#         self.train_X, self.train_y = None, None
#         self.params = {"l": 0.5, "sigma_f": 0.2}
#         self.optimize = optimize

#     def fit(self, X, y):
#         # store train data
#         self.train_X = np.asarray(X)
#         self.train_y = np.asarray(y)
#         self.is_fit = True

#     def predict(self, X):
#         if not self.is_fit:
#             print("GPR Model not fit yet.")
#             return

#         X = np.asarray(X)
#         Kff = self.kernel(self.train_X, self.train_X)  # (N, N)
#         Kyy = self.kernel(X, X)  # (k, k)
#         Kfy = self.kernel(self.train_X, X)  # (N, k)
#         Kff_inv = np.linalg.inv(Kff + 1e-8 * np.eye(len(self.train_X)))  # (N, N)
        
#         mu = Kfy.T.dot(Kff_inv).dot(self.train_y)
#         cov = Kyy - Kfy.T.dot(Kff_inv).dot(Kfy)
#         return mu, cov

#     def kernel(self, x1, x2):
#         dist_matrix = np.sum(x1**2, 1).reshape(-1, 1) + np.sum(x2**2, 1) - 2 * np.dot(x1, x2.T)
#         return self.params["sigma_f"] ** 2 * np.exp(-0.5 / self.params["l"] ** 2 * dist_matrix)


# if __name__ =="__main__":
#     # def y(x, noise_sigma=0.0):
#     #     x = np.asarray(x)
#     #     y = np.cos(x) + np.random.normal(0, noise_sigma, size=x.shape)
#     #     return y.tolist()

#     # train_X = np.array([3, 1, 4, 5, 9]).reshape(-1, 1)
#     # train_y = y(train_X, noise_sigma=1e-4)
#     # test_X = np.arange(0, 10, 0.1).reshape(-1, 1)

#     # gpr = GPR()
#     # gpr.fit(train_X, train_y)
#     # mu, cov = gpr.predict(test_X)
#     # test_y = mu.ravel()
#     # uncertainty = 1.96 * np.sqrt(np.diag(cov))
#     # plt.figure()
#     # plt.title("l=%.2f sigma_f=%.2f" % (gpr.params["l"], gpr.params["sigma_f"]))
#     # plt.fill_between(test_X.ravel(), test_y + uncertainty, test_y - uncertainty, alpha=0.1)
#     # plt.plot(test_X, test_y, label="predict")
#     # plt.scatter(train_X, train_y, label="train", c="red", marker="x")
#     # plt.legend()
#     # plt.show()

#     def y_2d(x, noise_sigma=0.0):
#         x = np.asarray(x)
#         y = np.sin(0.5 * np.linalg.norm(x, axis=1))
#         y += np.random.normal(0, noise_sigma, size=y.shape)
#         return y

#     train_X = np.random.uniform(-4, 4, (100, 2)).tolist()
#     train_y = y_2d(train_X, noise_sigma=1e-4)

#     test_d1 = np.arange(-5, 5, 0.2)
#     test_d2 = np.arange(-5, 5, 0.2)
#     test_d1, test_d2 = np.meshgrid(test_d1, test_d2)
#     test_X = [[d1, d2] for d1, d2 in zip(test_d1.ravel(), test_d2.ravel())]

#     gpr = GPR(optimize=True)
#     gpr.fit(train_X, train_y)
#     mu, cov = gpr.predict(test_X)
#     z = mu.reshape(test_d1.shape)

#     fig = plt.figure(figsize=(7, 5))
#     ax = Axes3D(fig)
#     ax.plot_surface(test_d1, test_d2, z, linewidth=0, alpha=0.2, antialiased=False)
#     ax.scatter(np.asarray(train_X)[:,0], np.asarray(train_X)[:,1], train_y, c=train_y)
#     ax.contourf(test_d1, test_d2, z, zdir='z', offset=0, alpha=0.6)
#     ax.set_title("l=%.2f sigma_f=%.2f" % (gpr.params["l"], gpr.params["sigma_f"]))


#高斯过程拟合
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.gaussian_process import GaussianProcessRegressor
# from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# # 生成数据集
# np.random.seed(42)
# days = np.arange(1, 31)
# power = 50 + 0.5 * days + np.random.normal(0, 5, len(days))
# weapon_skill = 50 + 0.3 * days + np.random.normal(0, 5, len(days))
# battle_win_rate = 0.3 * power + 0.7 * weapon_skill + np.random.normal(0, 5, len(days))

# data = pd.DataFrame({
#     '天数': days,
#     '功力': power,
#     '武器熟练度': weapon_skill,
#     '战斗胜率': battle_win_rate
# })

# # 提取特征和目标变量
# X = data[['天数']].values
# y = data['战斗胜率'].values


# # 定义高斯过程回归模型
# kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))
# gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# # 训练模型
# gp.fit(X, y)

# # 生成一组测试数据
# X_test = np.linspace(1, 30, 100).reshape(-1, 1)

# # 预测战斗胜率
# y_pred, sigma = gp.predict(X_test, return_std=True)


# # 绘制拟合曲线和不确定性
# plt.figure(figsize=(10, 6))
# plt.scatter(X, y, c='b', label='real rate')
# plt.plot(X_test, y_pred, 'r', label='pred rate')
# plt.fill_between(X_test.flatten(), y_pred - 1.96 * sigma, y_pred + 1.96 * sigma, alpha=0.2, color='darkorange', label='95%')
# plt.xlabel('dates')
# plt.ylabel('rates')
# plt.title('GP prediction')
# plt.legend()
# plt.show()

#

from tqdm import tqdm
import time

n_clusters = 5

range_vec = tqdm(range(n_clusters))  #range_vec 是一个 tqdm 迭代器对象，可以像普通 range 一样用于 for 循环，但会显示进度条

# print(range_vec)

for cluster in range_vec:
    time.sleep(0.1)
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

tray = [[1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9]]
tray = np.array(tray)
print(np.arange(0, tray.shape[1], 3))
for i in np.arange(0, int(9), 3):
    item = int(i/3) #第item个维度求解
    # print(item)
    print(i)


c_p = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Row-major (C):", c_p.ravel())  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Column-major (F):", c_p.ravel(order='F'))  # [1, 4, 7, 2, 5, 8, 3, 6, 9]

from matplotlib.font_manager import FontManager
fm = FontManager()
available_fonts = [f.name for f in fm.ttflist]
print(available_fonts)