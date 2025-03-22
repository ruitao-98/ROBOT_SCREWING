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



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# 生成数据集
np.random.seed(42)
days = np.arange(1, 31)
power = 50 + 0.5 * days + np.random.normal(0, 5, len(days))
weapon_skill = 50 + 0.3 * days + np.random.normal(0, 5, len(days))
battle_win_rate = 0.3 * power + 0.7 * weapon_skill + np.random.normal(0, 5, len(days))

data = pd.DataFrame({
    '天数': days,
    '功力': power,
    '武器熟练度': weapon_skill,
    '战斗胜率': battle_win_rate
})

# 提取特征和目标变量
X = data[['天数']].values
y = data['战斗胜率'].values


# 定义高斯过程回归模型
kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# 训练模型
gp.fit(X, y)

# 生成一组测试数据
X_test = np.linspace(1, 30, 100).reshape(-1, 1)

# 预测战斗胜率
y_pred, sigma = gp.predict(X_test, return_std=True)


# 绘制拟合曲线和不确定性
plt.figure(figsize=(10, 6))
plt.scatter(X, y, c='b', label='real rate')
plt.plot(X_test, y_pred, 'r', label='pred rate')
plt.fill_between(X_test.flatten(), y_pred - 1.96 * sigma, y_pred + 1.96 * sigma, alpha=0.2, color='darkorange', label='95%')
plt.xlabel('dates')
plt.ylabel('rates')
plt.title('GP prediction')
plt.legend()
plt.show()
