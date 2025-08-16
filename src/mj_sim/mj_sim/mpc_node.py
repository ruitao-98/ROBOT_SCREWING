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
from mpc_optimizer import Mpc_Opti
import trajectory_planner as traj
import numpy as np
from robot_msgs.msg import ControlCommand
from robot_msgs.msg import RobotStatus 
import threading
from std_srvs.srv import Trigger
import time
from robot_msgs.srv import StartPose
import results_plots as rp

class MPCWrapper(Node):
    def __init__(self):
        super().__init__("mpc_node")  # 初始化节点，命名为 'mpc_node'
        # 变量和类继承
        self.mpc_optimzer = Mpc_Opti(gp_regressors=None, B_x=None)
        self.N = self.mpc_optimzer.N
        self.n_controls = self.mpc_optimzer.n_controls
        self.n_states = self.mpc_optimzer.n_controls

        # 声明参数并提供默认值
        self.declare_parameter('t0', 0.0)
        self.declare_parameter('traj_length', 0.18)
        self.declare_parameter('speed', 0.01)
        self.declare_parameter('dt', 0.008)
        self.declare_parameter('position_sequence', [0.0, 0.0, 0.0])
        self.declare_parameter('orientation_sequence', [1.0, 0.0, 0.0, 0.0])

        # 获得参数，重新生成轨迹，用于mpc计算
        t0 =                   self.get_parameter('t0').value
        traj_length =          self.get_parameter('traj_length').value
        speed =                self.get_parameter('speed').value
        dt =                   self.get_parameter('dt').value
        position_sequence =    np.array([self.get_parameter('position_sequence').value])
        orientation_sequence = np.array([self.get_parameter('orientation_sequence').value])

        trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = traj.generate_straight_trajectory(traj_length, dt, 
                                                                                                                                                speed, position_sequence, 
                                                                                                                                                orientation_sequence) #生成x方向的直线轨迹
        # trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = traj.generate_rectangular_trajectory(traj_length, dt, 
        #                                                                                                                                         speed, position_sequence, 
        #                                                                                                                                         orientation_sequence) #生成x方向的直线轨迹
        
        # trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = traj.generate_triangular_trajectory(traj_length, dt, 
        #                                                                                                                                            speed, position_sequence, 
        #                                                                                                                                            orientation_sequence) #生成x方向的直线轨迹
        self.pos_para = [0, 0, 0]
        self.ori_para = [0, 0, 0, 1]
        #推理用时
        self.Time = []

        self.mpc_counter = 0
        traj_1 = np.hstack((trajectory_positions[:, [0]], trajectory_velocities[:, [0]]))
        traj_1 = np.hstack((traj_1, np.zeros((len(trajectory_positions), 1))))
        traj_2 = np.hstack((trajectory_positions[:, [1]], trajectory_velocities[:, [1]]))
        traj_2 = np.hstack((traj_2, np.zeros((len(trajectory_positions), 1))))
        traj_3 = np.hstack((trajectory_positions[:, [2]], trajectory_velocities[:, [2]]))
        traj_3 = np.hstack((traj_3, np.zeros((len(trajectory_positions), 1))))

        # traj_2 = np.hstack((trajectory_positions[:, [1]], np.zeros((len(trajectory_positions), 1))))
        # traj_2 = np.hstack((traj_2, np.zeros((len(trajectory_positions), 1))))
        # traj_1 = np.hstack((trajectory_positions[:, [0]],np.zeros((len(trajectory_positions), 1))))
        # traj_1 = np.hstack((traj_1, np.zeros((len(trajectory_positions), 1))))

        self.traj_all =  np.hstack((traj_1, traj_2, traj_3)) # x * 9，只包括x y z 不包括旋转
        np.savetxt('traj.txt', self.traj_all)
        # print(self.traj_all)

        self.traj_all_base = self.traj_all.copy()
      
        # 定义机器人状态变量
        self.eef_rotm = np.zeros((3,3))
        self.eef_pos = np.zeros(3)
        self.eef_vel = np.zeros(6)

        self.world_force = np.zeros(6)

        # 处理轨迹，根据当前状态更新期望参考轨迹，根据当前已经前进的步数，也就是self.current_idx变量，更新当前位置
        # 每次优化递增 1（self.current_idx += 1），与优化频率（25 Hz，每 40ms 一步）同步。
        self.current_idx = 0
        self.late_step = 2

        # 初始化单个维度的状态和控制量
        self.x0 = np.array([0.0, 0.0, 0.0]).reshape(-1, 1)  
        self.u0 = np.array([-600, -50, 1] * self.N).reshape(-1, 3).T   #  .T 后 是3 *N
        self.x_m = np.zeros((self.n_states, self.N + 1))
 
        self.next_states = self.x_m.copy()  #(3, N+1)
        self.optimize_next = True

        self.X0 = []
        self.U0 = []
        self.Xm = []
        self.Next_s = []
        for i in range(int(self.traj_all_base.shape[1]/3)):
            self.X0.append(self.x0.copy())               # 状态数组，每个单元（3,1）
            self.U0.append(self.u0.copy())               # 控制输入数组，每个单元（N,3）
            self.Xm.append(self.x_m.copy())              # 预测数组，每个单元（3,N+1）
            self.Next_s.append(self.next_states.copy())  # 预测后，产生动作后修正的状态数组，用于下次热启动，每个单元（N+1,3）
        
        # 订阅消息，回调函数中进行MPC的优化计算
        self.status_sub = self.create_subscription(RobotStatus, "rob_status", self.status_callback, 1)
        self.command_pub = self.create_publisher(ControlCommand, "rob_command", 1)

        self.client = self.create_client(StartPose, 'get_param')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for robot_sim_ready service...')
        self.get_logger().info("MPC Node started, calling robot_sim_env service")

        # 调用服务并等待响应
        self.call_service()
    
    def traj_transform(self, pos_para, ori_para):
        """
        把末端坐标系下生成的局部轨迹转化为机器人基坐标系下轨迹
        """
 
        # 转换为 NumPy
        start_pos_np = np.array(pos_para)
        start_rotm_np = np.array(ori_para).reshape(3, 3)

        for local_i in range(len(self.traj_all)):
            incre_pos = np.array([self.traj_all[local_i, 0], self.traj_all[local_i, 3], self.traj_all[local_i, 6]])
            action_pos = start_pos_np + start_rotm_np @ incre_pos
            incre_vel = np.array([self.traj_all[local_i, 1], self.traj_all[local_i, 4], self.traj_all[local_i, 7]])
            action_vel = start_rotm_np @ incre_vel

            assert action_pos.shape[0] == 3, "action_pos must have 3 elements"
            self.traj_all_base[local_i, [0, 3, 6]] = action_pos
            self.traj_all_base[local_i, [1, 4, 7]] = action_vel
        
        self.target_pos = self.traj_all_base[-1, [0, 3, 6]]  # 最终位置 (x, y, z)
        print("the traj is transformed!")
            
    
    def call_service(self):
        request = StartPose.Request()
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        # self.traj_transform()

        if future.result() is not None and future.result().success:
            self.get_logger().info("Received response from robot_sim_env, starting main logic")
            self.pos_para = future.result().pos_para
            self.ori_para = future.result().ori_para
            self.get_logger().info(f"Received pos_para: {self.pos_para}")
            self.get_logger().info(f"Received ori_para: {self.ori_para}")
            self.traj_transform(self.pos_para, self.ori_para)
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

        distance = np.linalg.norm(self.target_pos - self.eef_pos)  # 欧几里得距离
        threshold = 0.005  # 阈值，例如 1 毫米
        if distance < threshold and self.current_idx >= 1000:
            # 打印 Time 的均值
            if self.Time:
                time_mean = np.mean(self.Time)
                print(f"Time 均值: {time_mean:.2f} 毫秒")
                # 可视化 Time 变化图像
                # rp.plot_time(self.Time, time_mean)
            else:
                print("Time 数据为空，未执行优化")
            # 终止程序
            print("机器人已接近目标位置，程序终止")
            rclpy.shutdown()  # 关闭 ROS 节点
            sys.exit(0)  # 退出程序

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

        # if not self.optimize_next: #如果self.optimize_next=false，那么上一步刚刚优化过了，这一步不需要再优化了，我们等待上一步的线程结束即可。
        #     self.mpc_thread.join()
        #     self.optimize_next = True #
        #     return #这一步不优化，直接return结束函数

        # def _thread_func():
        #     self.run_mpc()

        # self.mpc_thread = threading.Thread(target=_thread_func(), args=(), daemon=True) #开启额外线程运行mpc计算，防止无法及时处理消息
        # self.mpc_thread.start()
        # self.optimize_next = False
    
    def run_mpc(self):
        ref_traj = self.set_reference()

        start_time = time.perf_counter()
        for i in np.arange(0, int(self.traj_all_base.shape[1])-3, 3):  # 只计算两个维度
            item = int(i/3) #第item个维度求解
            c_p = ref_traj[:, i:i+3].T  #3*N

            if(item == 0):
                # print("###item = 0###")
                # print("c_p:", c_p[:, 0])
                # print("f_x:", self.X0[item][2, 0])
                # print("state:", self.X0[item][:, 0])
                # print("k:", -self.U0[item][0, 0] * self.mpc_optimzer.c)
                # print("d:", -self.U0[item][1, 0] * self.mpc_optimzer.c)
                # print("State error:", self.Next_s[item][:, 0] - c_p[:, 0])
                # lower_bounds = [-0.01, -np.inf, -np.inf]
                # upper_bounds = [0.01,  np.inf, np.inf]
                Q_val = np.array([[100, 0.0, 0.0],
                                [0.0, 0.01, 0.0],
                                [0.0, 0.0, 0.1]])
                # Q_val = np.array([[700.0, 0.0, 0.0],
                #                 [0.0, 0.001, 0.0],
                #                 [0.0, 0.0, 0.001]])  #无障碍任务
                lower_bounds = [-np.inf, -np.inf, -np.inf]
                upper_bounds = [ np.inf,  np.inf,  np.inf]
                self.set_state_bounds(lower_bounds, upper_bounds)

            elif(item == 1):
                # print("###item = 1###")
                # print("c_p:", c_p[:, 0])
                # print("f_x:", self.X0[item][2, 0])
                # print("state:", self.X0[item][:, 0])
                # print("k:", -self.U0[item][0, 0] * self.mpc_optimzer.c)
                # print("d:", -self.U0[item][1, 0] * self.mpc_optimzer.c)
                # print("State error:", self.Next_s[item][:, 0] - c_p[:, 0])
                Q_val = np.array([[100.0, 0.0, 0.0],
                                [0.0, 0.01, 0.0],
                                [0.0, 0.0, 0.1]])  #有障碍任务

                # Q_val = np.array([[700.0, 0.0, 0.0],
                #                 [0.0, 0.001, 0.0],
                #                 [0.0, 0.0, 0.001]])  #无障碍任务
                lower_bounds = [-np.inf, -np.inf, -np.inf]
                upper_bounds = [ np.inf,  np.inf,  np.inf]
                # upper_bounds = [self.pos_para[1] + 0.06,  np.inf,  np.inf]
                self.set_state_bounds(lower_bounds, upper_bounds)
            
            else:
                Q_val = np.array([[1000.0, 0.0, 0.0],
                                [0.0, 0.001, 0.0],
                                [0.0, 0.0, 0.001]])

            delta_f_values = np.zeros(self.N)
            init_control = np.concatenate((self.U0[item].reshape(-1, 1, order='F'), self.Next_s[item].reshape(-1, 1, order='F'))) #U0来自于上一时刻优化结果，X0来自于ros的消息

            # zero_matrix1 = np.zeros_like(self.U0[item].reshape(-1, 1, order='F'))
            # zero_matrix2 = np.zeros_like(self.Next_s[item].reshape(-1, 1, order='F'))
            # init_control = np.concatenate((zero_matrix1, zero_matrix2)) #U0来自于上一时刻优化结果，X0来自于ros的消息

            c_p_flat = c_p.ravel(order='F')  # 改为 Fortran-style（列优先）

            # print("x0=", self.X0[item], 'x0_ravel=', self.X0[item].ravel(order='F'))
            p = np.concatenate((c_p_flat, self.X0[item].ravel(order='F'), delta_f_values, Q_val.ravel(order='F')))
            res = self.mpc_optimzer.solve(init_control, p)

            estimated_opt = res['x'].full() # 提取优化变量的结果，是一个MX，或者DX的对象，estimated_opt是优化变量的最终值，是一个一维数组。
            self.U0[item] = estimated_opt[:self.N*self.n_controls].reshape(self.N, self.n_controls).T  # (N, n_controls) 转化为(n_controls, N)
            self.Xm[item] = estimated_opt[self.N*self.n_controls:].reshape(self.N + 1, self.n_states).T   # (N+1, n_states) 预测的状态 转化为(n_states, N+1)
        
        end_time = time.perf_counter()
        self.Time.append((end_time - start_time) * 1000)
        print('curret time = ', (end_time - start_time) * 1000)
        # u = -k_x / m_x, -d_x / m_x, 1 / m_x
        command = ControlCommand()

        # command.d = [-self.U0[0][1, 0]/self.U0[0][2, 0], -self.U0[1][1, 0]/self.U0[1][2, 0], -self.U0[2][1, 0]/self.U0[2][2, 0], 1.0, 1.0, 1.0] #xyz的阻尼和刚度是求解的，其他三个维度暂时是写死的 m_x * u[1]
        # command.k = [-self.U0[0][0, 0]/self.U0[0][2, 0], -self.U0[1][0, 0]/self.U0[1][2, 0], -self.U0[2][0, 0]/self.U0[2][2, 0], 0.8, 0.8, 0.8] #xyz的阻尼和刚度是求解的，其他三个维度暂时是写死的, m_x * u[0]
        command.d = [-self.U0[0][1, self.late_step ]/self.U0[0][2, self.late_step ], -self.U0[1][1, self.late_step ]/self.U0[1][2, self.late_step ], 100.0, 1.0, 1.0, 1.0] #xyz的阻尼和刚度是求解的，其他三个维度暂时是写死的 m_x * u[1]
        command.k = [-self.U0[0][0, self.late_step ]/self.U0[0][2, self.late_step ], -self.U0[1][0, self.late_step ]/self.U0[1][2, self.late_step ], 1400.0, 0.8, 0.8, 0.8] #xyz的阻尼和刚度是求解的，其他三个维度暂时是写死的, m_x * u[0]

        self.command_pub.publish(command)
        print("****************************************")

    def set_state_bounds(self, lower_bounds, upper_bounds):
        """设置新的状态约束并更新边界"""
        """动态更新优化变量的上下界"""
        self.mpc_optimzer.lbx = []
        self.mpc_optimzer.ubx = []
        # 控制输入 U 的界限
        for _ in range(self.N):
            self.mpc_optimzer.lbx.extend(self.mpc_optimzer.input_lower_bounds)  # 控制输入下界
            self.mpc_optimzer.ubx.extend(self.mpc_optimzer.input_upper_bounds)  # 控制输入上界
        # 状态变量 X 的界限
        for _ in range(self.N + 1):
            self.mpc_optimzer.lbx.extend(lower_bounds)
            self.mpc_optimzer.ubx.extend(upper_bounds)

    def set_state(self):
        #解构机器人状态到mpc能识别的状态
        x0_0 = np.array([self.eef_pos[0], self.eef_vel[0], self.world_force[0]]).reshape(-1, 1) #3*1
        x0_1 = np.array([self.eef_pos[1], self.eef_vel[1], self.world_force[1]]).reshape(-1, 1)
        x0_2 = np.array([self.eef_pos[2], self.eef_vel[2], self.world_force[2]]).reshape(-1, 1)
        self.X0[0] = x0_0
        self.X0[1] = x0_1
        self.X0[2] = x0_2

        self.Next_s[0] = np.concatenate((x0_0, self.Next_s[0][:, 1:]), axis=1)
        self.Next_s[1] = np.concatenate((x0_1, self.Next_s[1][:, 1:]), axis=1)
        self.Next_s[2] = np.concatenate((x0_2, self.Next_s[2][:, 1:]), axis=1)
        self.U0[0] = np.concatenate((self.U0[0][:, 1:], self.U0[0][:, -1:]), axis=1)
        self.U0[1] = np.concatenate((self.U0[1][:, 1:], self.U0[1][:, -1:]), axis=1)
        self.U0[2] = np.concatenate((self.U0[2][:, 1:], self.U0[2][:, -1:]), axis=1) #更新状态集和控制输入集

    def set_reference(self):
        print(f"self.current_idx: {self.current_idx}, self.N: {self.N}")
        # print(f"self.traj_all_base.shape: {self.traj_all_base.shape}")
        ref_traj = self.traj_all_base[self.current_idx: self.current_idx + self.N + 1, :] #切片操作
        print(f"ref_traj.shape before padding: {ref_traj.shape}")
        while ref_traj.shape[0] < self.N + 1:
            if ref_traj.shape[0] == 0:
                print("Warning: ref_traj is empty, using last known position or default")
                ref_traj = np.zeros((1, self.traj_all_base.shape[1]))  # 默认填充
            ref_traj = np.concatenate((ref_traj, ref_traj[-1, :].reshape(1, -1)), axis=0)
        # print(f"ref_traj.shape after padding: {ref_traj.shape}")
        return ref_traj

def main():
    rclpy.init() 
    mpc_node = MPCWrapper()
    rclpy.spin(mpc_node)

if __name__ == "__main__":
    main()

