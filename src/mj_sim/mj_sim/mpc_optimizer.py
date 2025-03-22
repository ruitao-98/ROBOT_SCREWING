#! /home/yanji/anaconda3/envs/screwrobot/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
# print("当前 Python 解释器路径:", sys.executable)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print("当前 sys.path:", sys.path)  # 调试用

sys.path.append(f'/home/yanji/anaconda3/envs/screwrobot/lib/python3.8/site-packages')

import rclpy
from rclpy.node import Node
from robot_msgs.msg import FtPub

import casadi as ca
import casadi.tools as ca_tools
import matplotlib.pyplot as plt
import numpy as np
import time
import trajectory_planner as traj



class Mpc_Opti:

    def __init__(self):

        self.T = 0.008  # sampling time [s]
        self.N = 50  # prediction horizon 预测的节点数量

        self.k_min = 100
        self.k_max = 2000
        self.d_min = 20
        self.d_max = 200
        self.c = 2.5

        self.x = ca.SX.sym('x')
        self.x_dot = ca.SX.sym('x_dot')
        self.f_x = ca.SX.sym('f_x')
        self.s = ca.vertcat(self.x, self.x_dot, self.f_x)  # 机器人状态向量 (6,1)
        self.n_states = self.s.size()[0]

        self.x_r = ca.SX.sym('x_r')
        self.x_dot_r = ca.SX.sym('x_dot_r')
        self.f_xr = ca.SX.sym('f_xr')
        self.s_r = ca.vertcat(self.x_r, self.x_dot_r, self.f_xr)  # 目标状态

        self.n_controls = 3

        self.u = ca.SX.sym('u', self.n_controls)  # 控制输入矩阵

        # 定义状态误差
        self.s_tilde = self.s - self.s_r

        # 定义状态方程参数
        self.A = ca.SX.zeros(3, 3)
        self.A[0, 1] = 1

        self.b = ca.SX([0, 1, 0])
        self.beta = ca.SX([self.T/2, 0, 0])

        # 构建离散状态转移方程
        self.I = ca.SX.eye(3)  # 单位矩阵

        self.s_next = (self.A * self.T + self.I) @ self.s + self.T * ((self.b + self.beta) @ self.s_tilde.T @ self.u)  # 离散化方程

        self.f = ca.Function('f', [self.s, self.s_r, self.u], [self.s_next],
                        ['input_state', 'state_ref', 'control_input'], ['state_next'])
        # f_simple = ca.Function('f_simple', [s,  s_r, u], [s])

        # 构建MPC仿真
        # for MPC
        self.U = ca.SX.sym('U', self.n_controls, self.N)

        self.X = ca.SX.sym('X', self.n_states, self.N + 1)

        self.X_r = ca.SX.sym('X_r', self.n_states, self.N + 1)  # 参数的集合，此处代表从当前状态出发的一段参考轨迹 3 * n+1

        self.X0 = ca.SX.sym('X0', self.n_states)  # 当前状态作为参数

        # P = ca.SX.sym('P', n_states + n_states) #初始和终端

        # define

        self.Q = np.array([[100.0, 0.0, 0.0],
                    [0.0, 20, 0.0],
                    [0.0, 0.0, 100]])

        self.R = np.array([[1e-5, 0.0, 0.0],
                    [0.0, 1e-4, 0.0],
                    [0.0, 0.0, 1e-4]])

        # cost function
        self.obj = 0  # cost
        self.g = []  # equal constrains
        # self.g.append(self.X[:, 0] - self.X_r[:, 0]) #初始状态保持一致
        self.g = [self.X[:, 0] - self.X0]  # 初始状态固定为 X0

        for i in range(self.N):
            self.obj = (self.obj + ca.mtimes([(self.X[:, i] - self.X_r[:, i]).T, self.Q, self.X[:, i] - self.X_r[:, i]] ) )#控制输入
                                    # + ca.mtimes([self.U[:, i].T, self.R, self.U[:, i]])
                # + ca.mtimes([U[:, i].T, R, U[:, i]])) #控制输入
            self.x_next_ = self.f(self.X[:, i], self.X_r[:, i], self.U[:, i])
            self.g.append(self.X[:, i + 1] - self.x_next_)

        self.opt_variables = ca.vertcat(ca.reshape(self.U, -1, 1), ca.reshape(self.X, -1, 1))  # ca.reshape(U, -1, 1) 转换为一个列向量 6 * N, 1 casadi 默认列优先展平，这个和numpy不一样

        self.nlp_prob = {'f': self.obj, 'x': self.opt_variables, 'p': ca.horzcat(self.X_r, self.X0), 'g': ca.vertcat(*self.g)} # p: 列向量 3N+6
        self.opts_setting = {'ipopt.max_iter': 100, 'ipopt.print_level': 0, 'print_time': 0,
                    'ipopt.acceptable_tol': 1e-8, 'ipopt.acceptable_obj_change_tol': 1e-6}

        self.solver = ca.nlpsol('solver', 'ipopt', self.nlp_prob, self.opts_setting)

        self.lbg = 0.0
        self.ubg = 0.0 # g()函数等于0
        self.lbx = []
        self.ubx = []

        # 控制输入 U 的界限
        # u = -k_x / m_x, 
        #     -d_x / m_x,
        #      1 / m_x

        self.input_lower_bounds = [-self.k_max/self.c, -self.d_max/self.c, 1/self.c]
        self.input_upper_bounds = [-self.k_min/self.c, -self.d_min/self.c, 1/self.c]
        # 控制输入 U 的界限
        for _ in range(self.N):
            self.lbx.extend(self.input_lower_bounds)  # 控制输入下界
            self.ubx.extend(self.input_upper_bounds)  # 控制输入上界

        # 状态变量 X 的界限
        # s = ca.vertcat(x, y, x_dot, y_dot, f_x, f_y)  # 沿着y方向，所以我们在y方向不设约束，只设立x方向
        self.state_lower_bounds = [-np.inf, -np.inf, -np.inf]
        self.state_upper_bounds = [np.inf,  np.inf, np.inf]
        # 状态变量 X 的界限
        for _ in range(self.N + 1):
            self.lbx.extend(self.state_lower_bounds)
            self.ubx.extend(self.state_upper_bounds)
    
    def solve(self, init_control, c_p): 
        # 输入参数为：初始值和求解参数, 
        # 本次求解仅仅求解单次单个维度的最优解

        res = self.solver(x0=init_control, p=c_p, lbg=self.lbg,
            lbx=self.lbx, ubg=self.ubg, ubx=self.ubx)
        
        return res

def predict_next_state(mpc_opti, current_state, ref_state, control_input):
    """
    Predict the next state given the current state, reference state, and control input.
    
    Args:
        mpc_opti (Mpc_Opti): Instance of the Mpc_Opti class.
        current_state (np.ndarray): Current state [x, x_dot, f_x], shape (3,) or (3,1).
        ref_state (np.ndarray): Reference state [x_r, x_dot_r, f_xr], shape (3,) or (3,1).
        control_input (np.ndarray): Control input [u_0, u_1, u_2], shape (3,) or (3,1).
    
    Returns:
        np.ndarray: Next state [x_next, x_dot_next, f_x_next], shape (3,).
    """
# 确保输入为数值类型并转换为列向量
    s = np.array(current_state).reshape((3, 1))    # 当前状态
    s_r = np.array(ref_state).reshape((3, 1))      # 参考状态
    u = np.array(control_input).reshape((3, 1))    # 控制输入

    # 调用 CasADi 函数并求值
    s_next = mpc_opti.f(s, s_r, u)
    
    # 将 CasADi DM 类型转换为 NumPy 数组
    s_next_numeric = np.array(s_next).flatten()

    return s_next_numeric

if __name__ == "__main__":
    # 创建 Mpc_Opti 实例
    mpc = Mpc_Opti()

    # 示例输入
    current_state = np.array([0.0, 0.0, 10.0])      # [x, x_dot, f_x]
    ref_state = np.array([0.1, 0.1, 0.0])          # [x_r, x_dot_r, f_xr]
    control_input = np.array([-500.0, -100.0, 1/2.5])   # [u_0, u_1, u_2]

    # 预测下一状态
    next_state = predict_next_state(mpc, current_state, ref_state, control_input)
    print("Next state:", next_state)


