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
from pose_mpc_optimizer_withgp import Mpc_Opti
import trajectory_planner as traj
import numpy as np
from robot_msgs.msg import ControlCommand
from robot_msgs.msg import RobotStatus 
import threading
from std_srvs.srv import Trigger
import time
from robot_msgs.srv import StartRotation
import results_plots as rp
from scipy.spatial.transform import Rotation as R

import subprocess
from gp_model.utils import safe_mkdir_recursive, load_pickled_models
from gp_model.utils import distance_maximizing_points, get_model_dir_and_file
from config.configuration import ModelFitConfig as Conf
from gp_model.gp_common import restore_gp_regressors
from gp_model.utils import make_bx_matrix

"""
用于实际机器人旋拧任务的控制，特点有两点：
1. 期望轨迹是动态生成的，根据每一时刻的当前轨迹生成期望轨迹
2. 求解mpc的维度包括x y z rx ry
"""

class MPCWrapper(Node):
    def __init__(self):
        super().__init__("mpc_node")  # 初始化节点，命名为 'mpc_node'
        # 变量和类继承
                # 加载 GP 模型
        # git_version = '4196701'  # 长物体的实验结果
        git_version = "0826d04" # 短物体的实验结果
        # model_name = "simple_sim_gp"
        model_name = "real_task_gp"
        sim_options = Conf.ds_metadata
        load_ops = {"git": git_version, "model_name": model_name, "params": sim_options}

        # 为每个维度加载 GP 模型
        self.gp_models = {}
        self.B_x_dicts = {}
        global_dims = [2, 5, 8, 11, 14]  # x, y, z, rx, ry维度的全局索引
        for reg_y_dim in global_dims:  # 对应全局索引 2, 5, 8, 11, 14
            pre_trained_models = load_pickled_models(model_options=load_ops, dimension=reg_y_dim)
            if pre_trained_models is not None:
                gp_regressors = restore_gp_regressors(pre_trained_models)

                for gp_list in gp_regressors.gp.values():
                    for gp in gp_list:
                        gp.x_features = [0, 1, 2]  # 局部状态 [x, x_dot, f_x]
                        gp.u_features = []         # 假设控制输入 2 维

                self.gp_models[reg_y_dim] = gp_regressors # 字典
                # B_x = {}
                x_dims = 3  # 状态维度
                B_x = make_bx_matrix(x_dims, [2])  # 固定为 [2]，表示 f_x
                self.B_x_dicts[reg_y_dim] = B_x

            else:
                self.gp_models[reg_y_dim] = None
                self.B_x_dicts[reg_y_dim] = {}
        
        self.gp_models = [self.gp_models[global_dims[0]], self.gp_models[global_dims[1]], self.gp_models[global_dims[2]], 
                          self.gp_models[global_dims[3]], self.gp_models[global_dims[4]]]  # 需要你提供实际的 GPEnsemble 对象
        self.B_x_dicts = [self.B_x_dicts[global_dims[0]], self.B_x_dicts[global_dims[1]], self.B_x_dicts[global_dims[2]], 
                          self.B_x_dicts[global_dims[3]], self.B_x_dicts[global_dims[4]]]  # 需要你提供实际的 B_x 矩阵
        print('++++++++++++++++++++++++++++++++++++')
        self.mpc_optimizers = [
            Mpc_Opti(gp_regressors=self.gp_models[0], B_x=self.B_x_dicts[0]),
            Mpc_Opti(gp_regressors=self.gp_models[1], B_x=self.B_x_dicts[1]),
            Mpc_Opti(gp_regressors=self.gp_models[2], B_x=self.B_x_dicts[2]),
            Mpc_Opti(gp_regressors=self.gp_models[3], B_x=self.B_x_dicts[3]),
            Mpc_Opti(gp_regressors=self.gp_models[4], B_x=self.B_x_dicts[4])
        ]
        self.N = self.mpc_optimizers[0].N
        self.n_controls = self.mpc_optimizers[0].n_controls
        self.n_states = self.mpc_optimizers[0].n_controls
        print("current dim_idx = ",self.mpc_optimizers[0].dim_idx)
        print("current dim_idx = ",self.mpc_optimizers[1].dim_idx)
        print("current dim_idx = ",self.mpc_optimizers[2].dim_idx)
        print("current dim_idx = ",self.mpc_optimizers[3].dim_idx)
        print("current dim_idx = ",self.mpc_optimizers[4].dim_idx)
        self.rotation_speed = 46  # rev/s 46是参数，根据需要设置
        self.screw_pitch = 1.2 * 1e-3 #螺距 1.2 mm 
        self.speed = ((self.rotation_speed / 6.238) / 60) * self.screw_pitch # m/s

        # 获得参数，重新生成轨迹，用于mpc计算
        self.t0 =          0
        self.dt =          0.008
        self.position =    np.array([0.0, 0.0, 0.0])
        self.orientation = np.eye(3)

        # trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities 
        # #推理用时
        self.Time = []

        self.mpc_counter = 0
        self.traj_all = np.zeros((self.N, 15))
        
        # 定义机器人状态变量
        self.eef_rotm = np.zeros((3,3))
        self.eef_pos = np.zeros(3)
        self.eef_vel = np.zeros(6)

        self.world_force = np.zeros(6)
        self.late_step = 5
        # 处理轨迹，根据当前状态更新期望参考轨迹，根据当前已经前进的步数，也就是self.current_idx变量，更新当前位置
        # 每次优化递增 1（self.current_idx += 1），与优化频率（25 Hz，每 40ms 一步）同步。
        self.current_idx = 0

        # 初始化单个维度的状态和控制量
        self.x0 = np.array([0.0, 0.0, 0.0]).reshape(-1, 1)  
        self.u0 = np.array([-300, -50, 0.5] * self.N).reshape(-1, 3).T   #  .T 后 是3 *N
        self.x_m = np.zeros((self.n_states, self.N + 1))
 
        self.next_states = self.x_m.copy()  #(3, N+1)
        self.optimize_next = True

        self.X0 = []
        self.U0 = []
        self.Xm = []
        self.Next_s = []
        for i in range(5):  # x, y, z, rx, ry
            self.X0.append(self.x0.copy())               # 状态数组，每个单元（3,1）
            self.U0.append(self.u0.copy())               # 控制输入数组，每个单元（N,3）
            self.Xm.append(self.x_m.copy())              # 预测数组，每个单元（3,N+1）
            self.Next_s.append(self.next_states.copy())  # 预测后，产生动作后修正的状态数组，用于下次热启动，每个单元（N+1,3）
        
        # 订阅消息，回调函数中进行MPC的优化计算
        self.status_sub = self.create_subscription(RobotStatus, "rob_status", self.status_callback, 1)
        self.command_pub = self.create_publisher(ControlCommand, "rob_command", 1)

        self.client = self.create_client(StartRotation, 'get_rotation_param')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for robot_sim_ready service...')
        self.get_logger().info("MPC Node started, calling robot_sim_env service")

        # 调用服务并等待响应
        self.call_service()
    def call_service(self):
        request = StartRotation.Request()
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None and future.result().success:
            self.get_logger().info("Received response from robot_sim_env, starting main logic")
            self.rotation_speed = future.result().rotation_speed
            self.screw_pitch = future.result().screw_pitch
            self.speed = ((self.rotation_speed / 6.238) / 60) * self.screw_pitch # m/s
            pos_para = future.result().pos_para
            ori_para = future.result().ori_para
            self.position = np.array(pos_para)
            self.orientation = np.array(ori_para).reshape(3, 3)
        else:
            self.get_logger().error("Service call failed")

    def status_callback(self, msg):
        print("_________________update once_________________________")
        self.world_force = np.array(msg.ft_vector)
        self.eef_pos = np.array(msg.pos_vector)
        self.eef_rotm = np.array(msg.rotation_matrix).reshape(3,3)
        self.eef_vel = np.array(msg.vel_vector)
        self.set_state() #转化为MPC能理解的格式

        self.current_idx += 1 #每次回调函数被调用，都意味者仿真或者实机的控制周期前进了一步
        self.mpc_counter += 1

        if self.mpc_counter % self.late_step == 0:
        # 检查上一次线程是否完成
            if hasattr(self, 'mpc_thread') and self.mpc_thread.is_alive():
                print(f"MPC 线程仍在运行，跳过本次优化 (idx={self.current_idx})")
                return

            def _thread_func():
                self.run_mpc()

            self.mpc_thread = threading.Thread(target=_thread_func, args=(), daemon=True)
            self.mpc_thread.start()

    def run_mpc(self):
        # 生成一次轨迹
        
        ######
        trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = \
            traj.online_generate_straight_trajectory(self.N, self.dt, self.speed, self.position, self.orientation, self.eef_pos)
        # x, y, z 轨迹
        traj_1 = np.hstack((trajectory_positions[:, [0]], trajectory_velocities[:, [0]], np.zeros((self.N + 1, 1))))
        traj_2 = np.hstack((trajectory_positions[:, [1]], trajectory_velocities[:, [1]], np.zeros((self.N + 1, 1))))
        traj_3 = np.hstack((trajectory_positions[:, [2]], trajectory_velocities[:, [2]], np.zeros((self.N + 1, 1))))
        # rx, ry 轨迹（旋转向量为 0，角速度为 0，力矩为 0）,旋转向量的状态就是差值，所以期望直接设为0
        traj_4 = np.zeros((self.N + 1, 3))  # rx: [theta_x, omega_x, tau_x]
        traj_5 = np.zeros((self.N + 1, 3))  # ry: [theta_y, omega_y, tau_y]

        ref_traj = np.vstack((traj_1.T, traj_2.T, traj_3.T, traj_4.T, traj_5.T))  # 5×N×3

        start_time = time.perf_counter()
        for i in range(5):  # x, y, z, rx, ry
            c_p = ref_traj[i*3:(i+1)*3, :].copy()  # 3×N
            k_max = 2000
            k_min = 100
            d_max = 200
            d_min = 20
            c = 2.5
            lower_bounds = [-np.inf, -np.inf, -np.inf]
            upper_bounds = [np.inf, np.inf, np.inf]
            input_lower_bounds = [-k_max/c, -d_max/c, 1/c]
            input_upper_bounds = [-k_min/c, -d_min/c, 1/c]

            if i == 0: # x
                Q_val = np.array([[100.0, 0.0, 0.0],
                                [0.0, 10, 0.0],
                                [0.0, 0.0, 100]])
                self.mpc_optimizers[i].set_state_bounds(lower_bounds, upper_bounds, input_lower_bounds, input_upper_bounds)
            elif i == 1: # y
                Q_val = np.array([[1000.0, 0.0, 0.0],
                                [0.0, 1, 0.0],
                                [0.0, 0.0, 0.1]])
                self.mpc_optimizers[i].set_state_bounds(lower_bounds, upper_bounds, input_lower_bounds, input_upper_bounds)
            elif i == 2:  # z
                Q_val = np.array([[100.0, 0.0, 0.0],
                                 [0.0, 10, 0.0],
                                 [0.0, 0.0, 10]])
                self.mpc_optimizers[i].set_state_bounds(lower_bounds, upper_bounds, input_lower_bounds, input_upper_bounds)
            else: # rx, ry
                Q_val = np.array([[10.0, 0.0, 0.0],
                                [0.0, 10, 0.0],
                                [0.0, 0.0, 100]])
                k_max = 100
                k_min = 1
                d_max = 100
                d_min = 2
                c = 1
                lower_bounds = [-4 * np.pi/180, -3 * np.pi/180, -5] # 角度，角速度，力矩
                upper_bounds = [4 * np.pi/180, 3 * np.pi/180, 5]
                input_lower_bounds = [-k_max/c, -d_max/c, 1/c]
                input_upper_bounds = [-k_min/c, -d_min/c, 1/c]
                self.mpc_optimizers[i].set_state_bounds(lower_bounds, upper_bounds, input_lower_bounds, input_upper_bounds)
       
            # 动态选择GP模型
            if self.mpc_optimizers[i].with_gp:
                x_test = self.X0[i] - c_p[:, 0].reshape(-1, 1)  # 当前状态与参考状态的误差
                u_test = self.U0[i][:, 0].reshape(-1, 1)  # 当前控制输入
                u_data = [-u_test[0]/u_test[2], -u_test[1]/u_test[2]]
                gp_idx = self.mpc_optimizers[i].gp_regressors.select_gp(dim=self.mpc_optimizers[i].dim_idx, x=x_test, u=u_data)
                
                gp_idx = gp_idx[0] if isinstance(gp_idx, np.ndarray) else gp_idx  # 确保是标量
            else:
                gp_idx = 0
            print('selected gp_idx =',  gp_idx)
            init_control = np.concatenate((self.U0[i].reshape(-1, 1, order='F'), self.Next_s[i].reshape(-1, 1, order='F'))) #U0来自于上一时刻优化结果，X0来自于ros的消息
            c_p_flat = c_p.ravel(order='F')  # 改为 Fortran-style（列优先）
            trigger_values = np.zeros(self.N)
            trigger_values[0] = 1  # 仅第一个节点启用GP
            # print("x0=", self.X0[item], 'x0_ravel=', self.X0[item].ravel(order='F'))
            p = np.concatenate((c_p_flat, self.X0[i].ravel(order='F'), Q_val.ravel(order='F'), trigger_values))
            # res = self.mpc_optimzer.solve(init_control, p)
            res = self.mpc_optimizers[i].solve(init_control, p, gp_idx=gp_idx)
            estimated_opt = res['x'].full() # 提取优化变量的结果，是一个MX，或者DX的对象，estimated_opt是优化变量的最终值，是一个一维数组。
            self.U0[i] = estimated_opt[:self.N*self.n_controls].reshape(self.N, self.n_controls).T  # (N, n_controls) 转化为(n_controls, N)
            self.Xm[i] = estimated_opt[self.N*self.n_controls:].reshape(self.N + 1, self.n_states).T   # (N+1, n_states) 预测的状态 转化为(n_states, N+1)
        
        end_time = time.perf_counter()
        self.Time.append((end_time - start_time) * 1000)
        print('curret time = ', (end_time - start_time) * 1000)
        # u = -k_x / m_x, -d_x / m_x, 1 / m_x
        command = ControlCommand()
        command.d = [-self.U0[0][1, self.late_step]/self.U0[0][2, self.late_step], -self.U0[1][1, self.late_step]/self.U0[1][2, self.late_step], 
                     -self.U0[2][1, self.late_step]/self.U0[2][2, self.late_step], 
                    -self.U0[3][1, self.late_step]/self.U0[3][2, self.late_step], -self.U0[4][1, self.late_step]/self.U0[4][2, self.late_step], 1.0] 
        command.k = [-self.U0[0][0, self.late_step]/self.U0[0][2, self.late_step], -self.U0[1][0, self.late_step]/self.U0[1][2, self.late_step], 
                     -self.U0[2][0, self.late_step]/self.U0[2][2, self.late_step], 
                    -self.U0[3][0, self.late_step]/self.U0[3][2, self.late_step], -self.U0[4][0, self.late_step]/self.U0[4][2, self.late_step], 0.8] #xyzrxry的阻尼和刚度是求解的，其他维度暂时是写死的, m_x * u[0]

        self.command_pub.publish(command)
        print("****************************************")

    def set_state(self):
         # 计算旋转误差（轴角表示）
        e_rotm = self.eef_rotm @ self.orientation.T
        rotation = R.from_matrix(e_rotm)
        angle = rotation.magnitude()
        axis = rotation.as_rotvec() / angle if angle != 0 else np.zeros(3)
        rotation_vector = angle * axis
        #解构机器人状态到mpc能识别的状态
        x0_0 = np.array([self.eef_pos[0], self.eef_vel[0], self.world_force[0]]).reshape(-1, 1) #3*1
        x0_1 = np.array([self.eef_pos[1], self.eef_vel[1], self.world_force[1]]).reshape(-1, 1)
        x0_2 = np.array([self.eef_pos[2], self.eef_vel[2], self.world_force[2]]).reshape(-1, 1)
         # rx, ry 状态（旋转向量 x, y 分量）
        x0_3 = np.array([rotation_vector[0], self.eef_vel[3], self.world_force[3]]).reshape(-1, 1)  # rx
        x0_4 = np.array([rotation_vector[1], self.eef_vel[4], self.world_force[4]]).reshape(-1, 1)  # ry

        self.X0[0] = x0_0
        self.X0[1] = x0_1
        self.X0[2] = x0_2
        self.X0[3] = x0_3
        self.X0[4] = x0_4

        for i in range(5):
            self.Next_s[i] = np.concatenate((self.X0[i], self.Next_s[i][:, 1:]), axis=1)
            self.U0[i] = np.concatenate((self.U0[i][:, 1:], self.U0[i][:, -1:]), axis=1)

def main():
    rclpy.init() 
    mpc_node = MPCWrapper()
    rclpy.spin(mpc_node)

if __name__ == "__main__":
    main()

