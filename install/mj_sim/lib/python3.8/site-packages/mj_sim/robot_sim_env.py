#! /home/yanji/anaconda3/envs/screwrobot/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
# print("当前 Python 解释器路径:", sys.executable)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print("当前 sys.path:", sys.path)  # 调试用

sys.path.append(f'/home/yanji/anaconda3/envs/screwrobot/lib/python3.8/site-packages')

import mujoco
import mujoco.viewer
import numpy as np
import time


import gym
from gym import spaces, register
import transforms3d.quaternions as trans_quat
import transforms3d.euler as trans_eul
import copy
from scipy.spatial.transform import Rotation as R
# from source.lrmate_kine_base import IK
import robot_kinetic as ki
from robot_kinetic import RobotKdl
import rclpy
from rclpy.node import Node
from robot_msgs.msg import FtPub
import trajectory_planner as traj

# import rospy
# from robot_planning.msg import force_pub
# from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal

from sensor_msgs.msg import JointState
# import actionlib
import threading
from math import sin, cos
from robot_msgs.msg import RobotStatus
from robot_msgs.msg import ControlCommand
from std_srvs.srv import Trigger
from robot_msgs.srv import StartPose
from robot_msgs.msg import RefStatus

# from ray.tune.registry import register_env

class Dual_arm_env(gym.Env):
    def __init__(self, render=True):
        super(Dual_arm_env, self).__init__()

        self.lock = threading.Lock()
        # self.m = mujoco.MjModel.from_xml_path('./source/LRMate_200iD.xml')
        self.m = mujoco.MjModel.from_xml_path('/home/yanji/robot_screwing/src/mj_sim/model/xml/robot_arm.xml') 
        self.d = mujoco.MjData(self.m)
        self.kdl = RobotKdl(self.m, self.d)
        #ids that are need in the calculation

        self.link_6_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_BODY, 'right_link6')
        self.joint_6_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_JOINT, "r_j6")


        self.force_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_SENSOR, "r_force_sensor")
        self.torque_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_SENSOR, "r_torque_sensor")

        self.actuator_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_ACTUATOR, "r_motor6")

        self.screw_shaft_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_ACTUATOR, "r_p_screw")

        # joint control gains & variables
        # self.joint_kp = np.array([2000, 2000, 2000, 2000, 2000, 2000])  #关节pd控制器
        self.joint_kp = 2000 * np.ones(6)  # 关节pd控制器
        self.joint_kd = 2 * np.sqrt(self.joint_kp)  #关节pd控制器


        self.joint_pos = np.zeros(6)
        self.joint_vel = np.zeros(6)
        self.joint_acc = np.zeros(6)

        self.ref_joint = np.zeros(6)
        self.ref_vel = np.zeros(6)
        self.ref_acc = np.zeros(6)

        # self.gripper_pose = 0.031

        # self.set_gripper(self.gripper_pose)  # 夹爪宽度

        # admittance control gains
        self.adm_k = 1400 * np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])  # [10 10 10 10 10 10]
        self.adm_m = 2 * np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        self.adm_d = 4 * np.sqrt(np.multiply(self.adm_k,
                                              self.adm_m))  # [12.64911064 12.64911064 12.64911064 12.64911064 12.64911064 12.64911064] 4 * 10 ^ (-0.5)


        self.adm_pose_ref = np.zeros(7)  # 机器人导纳控制目标位姿
        self.adm_vel_ref = np.zeros(6)
        self.eef_vel = np.zeros(6)
        self.HZ = 125
        self._first_run = True #记录是否第一次循环

        # robot base pose
        base_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_BODY, 'right_link0')
        self.base_pos = self.d.xpos[base_id]
        self.base_rotm = self.d.xmat[base_id].reshape([3,3])

        # place holder for robot state
        self.pose_ = np.zeros(7)  # pose of link6, not the end-effector
        self.force_sensor_data = np.zeros(6)
        self.world_force = np.zeros(6)
        self.force_offset = np.zeros(6)
        self.world_force_filtered = np.zeros(6)

        self.eef_rotm = np.zeros((3,3))
        self.eef_pos = np.zeros(3)
        # self.jacobian = np.zeros((6, 6))

        # eef and force sensor offset setting

        self.eef_offset = np.array([-0.0785, 0, 0.0644 + 0.0525])
        self.eef_offset_rotm = trans_quat.quat2mat([1.34924e-11, -3.67321e-06, 1, -3.67321e-06])  # 注意四元数的顺序可能需要与库相对应

        
        self.eef_offset_to_sensor = np.array([-0.0785, 0, 0.013 + 0.0644])  # 传感器局部坐标系下TCP的位置
        self.eef_offset_rotm_to_sensor = trans_quat.quat2mat([1.34924e-11, -3.67321e-06, 1, -3.67321e-06])  #姿态

        self.force_frame_offset = np.array([0.00044323, -0.00044323, 0.0395])

        ####################
        self.work_space_xy_limit = 4
        self.work_space_z_limit = 8
        self.work_space_rollpitch_limit = np.pi * 5 / 180.0  # x, y
        self.work_space_yaw_limit = np.pi * 10 / 180.0   # z
        self.work_space_origin = np.array([0.50, 0, 0.1])  # 工作目标位置的原点位置，即孔所在的位置
        self.work_space_origin_rotm = np.array([[0, 0, 1],
                                                [0, 1, 0],
                                                [-1, 0, 0]])  #这个没用了

        ####################
        # self.goal = np.array([0, 0, 0])
        # self.goal_ori = np.array([0, 0, 0])
        # self.noise_level = 0.2
        # self.ori_noise_level = 0.5
        # self.use_noisy_state = False
        # self.state_offset = np.zeros(18)  # 状态补偿
        # self.force_noise = False
        # self.force_noise_level = 0.2
        # self.force_limit = 20
        # self.evaluation = True  # self.Render
        # self.moving_pos_threshold = rclpy.init() 
        # RL setting
        # self.obs_high = [self.work_space_xy_limit, self.work_space_xy_limit, self.work_space_z_limit,
        #                  self.work_space_rollpitch_limit, self.work_space_rollpitch_limit, self.work_space_yaw_limit,
        #                  0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
        #                  10, 10, 10, 10, 10, 10]
        # self.obs_high = np.array(self.obs_high)  # 本代码没明显用途

        # self.observation_space = spaces.Box(low=-1., high=1., shape=self.get_RL_obs().shape,
        #                                     dtype=np.float32)  # self.get_RL_obs()
        # self.action_space = spaces.Box(low=-np.ones(12), high=np.ones(12), dtype=np.float32)  # np.ones(12)  # 用于和强化学习算法定义使用，状态空间和动作空间大小定义

        ######### 动作的限制 ##########
        self.action_vel_high = 0.1 * np.array([1, 1, 0.5, 1, 1, 1])
        self.action_vel_low = -0.1 * np.ones(6)

        self.action_pos_high = np.array([6.2832, 4.6251, 3.0543, 4.6251, 6.2832, 6.2832])
        self.action_pos_low =  -np.array([6.2832, 1.4835, 3.0543, 1.4835, 6.2832, 6.2832])

        self.action_kp_high = 200 * np.array([1, 1, 1, 1, 1, 1])
        self.action_kp_low = 1 * np.array([1, 1, 1, 1, 1, 1])


        ############ init #############
        self.render = render
        if self.render:
            self.viewer = mujoco.viewer.launch_passive(self.m, self.d)  # mujoco 自带可视化工具，可视化
            # 假设 viewer 是通过之前代码段创建的
            self.viewer.cam.lookat[:] = [0.3, 0.8, 0.4]  # 设置新的焦点
            self.viewer.cam.distance = 2.4  # 设置相机到焦点的距离
            self.viewer.cam.azimuth = 10  # 设置水平旋转角度
            self.viewer.cam.elevation = -30  # 设置仰角
        # self.reset()
        # mujoco.mj_step(self.m, self.d)  # 前进

        # get robot state
        self.update_pose_vel()  # 位置、速度
        self.get_force_sensor_data()  # 力
        self.force_calibration()  # 力标定

        _eef_pos, _eef_rotm = self.reset()
        _eef_quat = trans_quat.mat2quat(_eef_rotm)

        action_pose = np.concatenate([_eef_pos, _eef_quat]) #当前eef的位姿（7，1), 设位初始期望位姿
        action_vel = np.zeros(6) #期望速度
        self.start_pose_quat = action_pose.copy()

        # 记住初始位置
        self.start_pos = action_pose[:3].copy()
        self.start_rotm = trans_quat.quat2mat(action_pose[3:]).copy()

        # 转换为 Python 列表
        start_pos_list = self.start_pos.tolist()  # 转换为 [x, y, z] 列表
        start_rotm_flat = self.start_rotm.flatten().tolist()  # 展平为 [r11, r12, r13, r21, r22, r23, r31, r32, r33] 列表

        # ros2 启动
        rclpy.init()  # 初始化ROS2客户端库
        # 创建节点实例
        self.node = Node("robot_sim")
        self.node.get_logger().info("robot-sim start!")

        # 设置 ROS 2 参数
        self.node.declare_parameter('pos_para', start_pos_list)
        self.node.declare_parameter('ori_para', start_rotm_flat)
        
        # 创建发布者
        self.force_pub = self.node.create_publisher(FtPub, "ft_data", 1)

        self.status_pub = self.node.create_publisher(RobotStatus, "rob_status", 1)
        self.ref_pub = self.node.create_publisher(RefStatus, "ref_status", 1) #用于记录，形成数据集
        self.cmd_pub = self.node.create_publisher(ControlCommand, "cmd_status", 1) #用于记录，形成数据集

        self.command_subs = self.node.create_subscription(ControlCommand, "rob_command", self.command_callback, 1)

        self.srv = self.node.create_service(StartPose, 'get_param', self.ready_callback)
        self.node.get_logger().info("Robot Sim Env started, waiting for MPC Node request...")

        time.sleep(1)

        self.start_time = time.time() # 仿真开始时间

    
    def ready_callback(self, request, response):
        self.node.get_logger().info("Received request from MPC Node, sending response")
        # 获取参数值
        pos_para = self.node.get_parameter('pos_para').get_parameter_value().double_array_value
        ori_para = self.node.get_parameter('ori_para').get_parameter_value().double_array_value

        pos_para_list = list(pos_para)  # 从 array('d', ...) 转为 [float, float, float]
        ori_para_list = list(ori_para)

        response.success = True
        response.message = "Robot Sim Env is ready"
        print(pos_para)
        response.pos_para = pos_para_list  # 3个元素的数组
        response.ori_para = ori_para_list  # 9个元素的数组

        return response
    
    def command_callback(self, msg):
        self.adm_k = np.array(msg.k, dtype=np.float64) 
        self.adm_d = np.array(msg.d, dtype=np.float64)
        # print(self.adm_d)
        


    def force_calibration(self, H=100):
        """
        Calibrate force sensor reading
        H: force history horizon
        """
        force_history = np.zeros([H, 6])
        self.sim_step()  #sim_step
        self.set_reference_traj(
            self.joint_pos, 0 * self.joint_vel, 0 * self.joint_acc
        )
        for _ in range(H):
            self.sim_step()
            force_history[_, :] = self.force_sensor_data
        self.force_offset = np.mean(force_history[int(H / 2):], axis=0)


    def update_pose_vel(self):
        # 更新 link6 的位置（位置+四元数位姿）和关节位置，速度（6*1）

        link6_pos = self.d.xpos[self.link_6_id]
        link6_rotm = self.d.xmat[self.link_6_id].reshape([3, 3])

        trans_right = self.base_rotm.T    
        link6_pos_base = trans_right @ (link6_pos - self.base_pos)
        link6_rotm_base = trans_right @  link6_rotm

        link6_rot_quat = trans_quat.mat2quat(link6_rotm_base)

        self.pose_ = np.concatenate([link6_pos_base, link6_rot_quat]) #(3 + 4) = 7

        self.joint_pos = self.d.qpos[self.joint_6_id - 5 :self.joint_6_id  + 1].copy()
        self.joint_vel = self.d.qvel[self.joint_6_id - 5 :self.joint_6_id + 1].copy()

        return self.pose_
    
    def get_link6_pose_(self, eef_pos, eef_rotm):

        link6_pos = eef_pos - eef_rotm @ (self.eef_offset_rotm.T @ self.eef_offset)
        link6_rotm = eef_rotm @ self.eef_offset_rotm.T

        #齐次坐标系下刚体运动的速度和角速度分析
        # https://gaoyichao.com/Xiaotu/?book=math_physics_for_robotics&title=%E5%A4%9A%E4%B8%AA%E5%9D%90%E6%A0%87%E7%B3%BB%E4%B8%8B%E7%9A%84%E9%80%9F%E5%BA%A6%E5%92%8C%E8%A7%92%E9%80%9F%E5%BA%A6%E5%88%86%E6%9E%90
        return link6_pos, link6_rotm
    

    def get_eef_pose_(self, link6_pose_): #link6->eef

        link6_pos = link6_pose_[:3]
        link6_rotm = trans_quat.quat2mat(link6_pose_[3:7])
        # right_eef_pos = right_link6_pos + right_link6_rotm @ self.right_eef_offset
        self.eef_rotm = link6_rotm @ self.eef_offset_rotm
        self.eef_pos = link6_pos + self.eef_rotm @ (self.eef_offset_rotm.T @ self.eef_offset)

        return self.eef_pos, self.eef_rotm
    
        
    def get_force_sensor_data(self):
        # get force sensor data

        f_adr = self.m.sensor_adr[self.force_id]
        f_dim = self.m.sensor_dim[self.force_id]
        force = np.copy(self.d.sensordata[f_adr:f_adr + f_dim])

        # get torque sensor data
        t_adr = self.m.sensor_adr[self.torque_id]
        t_dim = self.m.sensor_dim[self.torque_id]
        torque = np.copy(self.d.sensordata[t_adr:t_adr + t_dim])

        self.force_sensor_data = -np.concatenate([force, torque])

        return self.force_sensor_data

    def get_tcp_force(self):
    # tcp_force.head<3>() = eef_offset_rotm_to_sensor.transpose() * local_force.head<3>();
    # tcp_force.tail<3>() = -eef_offset_to_sensor.cross(tcp_force.head<3>()) + eef_offset_rotm_to_sensor.transpose() * local_force.tail<3>();

        self.world_force[:3] = self.eef_offset_rotm_to_sensor.T @ self.force_sensor_data[:3] #变换到TCP坐标系
        self.world_force[3:] = self.eef_offset_rotm_to_sensor.T @ self.force_sensor_data[3:] - np.cross(self.eef_offset_to_sensor, self.force_sensor_data[:3])
        self.world_force[:3] = self.eef_rotm @ self.world_force[:3] #变换到机器人的基坐标系
        self.world_force[3:] = self.eef_rotm @ self.world_force[3:]
        

    def joint_space_step(self, action):

        target_pos = action
        # keep the same action for a short time
        for i in range(100):
            done = False
            self.set_joint_pos(target_pos)
            self.sim_step()


    def admittance_control(self, ctl_ori=False):
        T = 1/self.HZ
        #当前位置和期望位置
        eef_pos, eef_rotm = self.get_eef_pose_(self.pose_)
        link6_pos, link6_rotm = self.get_link6_pose_(eef_pos, eef_rotm)

        eef_pos_d, eef_rotm_d = self.adm_pose_ref[:3], trans_quat.quat2mat(self.adm_pose_ref[3:7])

        #当前速度和期望速度
        eef_vel = self.eef_vel.copy()
        eef_desired_vel = self.adm_vel_ref.copy()

        #力，转化为机器人基坐标系下的力
        self.get_force_sensor_data()
        # self.force_sensor_data[:3] = self.force_sensor_data[:3] - self.force_offset[:3]  #compensate gravity
        # self.force_sensor_data[3:] = self.force_sensor_data[3:] - self.force_offset[3:]
        self.force_sensor_data[:3] = self.force_sensor_data[:3] #compensate gravity
        self.force_sensor_data[3:] = self.force_sensor_data[3:]
        self.get_tcp_force() #变换为world_force

        # if self.force_noise:
        #     self.world_force = self.world_force + np.random.normal(0, self.force_noise_level, 6)
        self.world_force = np.clip(self.world_force, -50, 50)  # 力的大小进行限制



        # 平滑力数据
        alpha = 0.2
        if self._first_run:
            self.world_force_filtered = self.world_force.copy()  # 首次运行时重新初始化
            self._first_run = False
        self.world_force_filtered = alpha * self.world_force_filtered + (1 - alpha) * self.world_force

        wish_force = np.array([0, 0, 0, 0, 0, 0])
        force_error = wish_force + self.world_force_filtered

        # msg = FtPub()
        # msg.fx = world_force_filtered[0]
        # msg.fy = world_force_filtered[1]
        # msg.fz = world_force_filtered[2]
        # msg.tx = world_force_filtered[3]
        # msg.ty = world_force_filtered[4]
        # msg.tz = world_force_filtered[5]
        # self.force_pub.publish(msg)

        # dynamics
        e = np.zeros(6)
        adm_pos = np.zeros(3)
        adm_rotm = np.zeros((3,3))

        e[:3] = eef_pos - eef_pos_d  #所有的这些位置差距都被变化到世界坐标系下（机器人基坐标系）进行表示，包括这里的eef_pos也是在世界坐标系下的一种表示。
        e_rotm = eef_rotm @ eef_rotm_d.T

        e_quat = trans_quat.mat2quat(e_rotm)
        quat_R = R.from_quat(e_quat)
        e[3:] = quat_R.as_rotvec()
        e[3:] = np.around(e[3:], decimals=6)

        e_dot = eef_vel - eef_desired_vel
        MA = 1 * force_error - np.multiply(self.adm_k, e) - np.multiply(self.adm_d, e_dot)
        adm_acc = np.divide(MA, self.adm_m)
        # right_adm_acc = np.linalg.inv(self.adm_m) @ MA
        adm_acc = np.around(adm_acc, decimals=6)

        adm_vel = self.eef_vel + adm_acc * T

        linear_disp = (adm_vel[:3]*T).flatten()
        angular_disp = (adm_vel[3:]*T).flatten()

        self.eef_vel = adm_vel.copy()

        return linear_disp, angular_disp

    def admittance_step_test(self, action_pose, action_vel, stop):

        # print(self.adm_k)
        # print(self.adm_d)

        # 全流程跟踪测试#
        self.update_pose_vel()
        
        desired_pose = action_pose.copy()  #期望位姿

        desired_pos = desired_pose[:3]
        desired_rotm = trans_quat.quat2mat(desired_pose[3:])
        self.adm_pose_ref[:3] = desired_pos.copy() 
        self.adm_pose_ref[3:7] = trans_quat.mat2quat(desired_rotm) #获取期望位姿，将位置+四元数转化为位置+旋转矩阵

        link6_linear, link6_angular = self.get_link6_pose_(desired_pos, desired_rotm)

        self.adm_vel_ref = action_vel.copy() 

        eef_pos, eef_rotm = self.get_eef_pose_(self.pose_) 

        # angular_vel = np.array([0,0,0])
        # # right_pos_vel = (right_desired_pos - right_eef_pos) * self.HZ_action
        # # right_desired_vel = np.concatenate([right_pos_vel, right_angular_vel])
        # # # right_angular_vel = np.array([0,0,0])
        # # right_desired_vel = np.array([0,0,0,0,0,0])

        # # self.right_adm_vel_ref = right_desired_vel
        # # self.adm_kp, self.adm_m 在类里面直接定义
        # force = np.array([0, 0, 0, 0, 0, 0])
        # peg_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_BODY, "peg")
        # self.d.xfrc_applied[peg_id, :] = force

        linear_disp, angular_disp = self.admittance_control() #输入期望速度，期望位置
        new_linear = eef_pos + linear_disp.reshape([3,])
        new_angular = desired_rotm.copy()
     

        link6_linear, link6_angular = self.get_link6_pose_(new_linear, new_angular) #变化为link6的速度
  
        q_target = self.kdl.ik(self.d.qpos[self.joint_6_id - 5: self.joint_6_id + 1], link6_linear,
                                     link6_angular)
        target_pos = q_target.copy()
    

        # keep the same action for a short time
        for i in range(int(1/(self.HZ * self.m.opt.timestep))):

            # if i == 0:
            #     eef_pos_old, eef_rotm_old = self.get_eef_pose_(self.pose_)
            self.set_joint_pos(target_pos)
            self.sim_step()
            eef_pos, eef_rotm = self.get_eef_pose_(self.pose_)

            # eef_pos, eef_rotm, eef_vel = self.get_eef_pose_(self.pose_)
            # link6_pos, link6_rotm, link6_vel = self.get_link6_pose_vel_from_eef(eef_pos, eef_rotm, desired_vel)

            ##差分获得机器人当前eef的速度

            # left_relative_rotm = R.from_matrix(left_eef_rotm) * R.from_matrix(left_eef_rotm_old).inv()
            # left_rotvec = left_relative_rotm.as_rotvec()


            # left_angular_vel = left_rotvec * self.HZ
            # left_pos_vel = (left_eef_pos - left_eef_pos_old) * self.HZ
            # self.left_eef_vel = np.concatenate([left_pos_vel, left_angular_vel])
            ##
            ######################测试注释掉######################

        self.status_publish()
        self.cmd_ref_publish(action_pose, action_vel, stop)

            # eef_pos_old, eef_rotm_old = self.get_eef_pose_(self.pose_)
    
    def cmd_ref_publish(self, desired_pose, desired_vel, stop):
        current_cmd = ControlCommand()
        print(list(self.adm_k))
        current_cmd.k = list(self.adm_k)
        current_cmd.d = list(self.adm_d)
        self.cmd_pub.publish(current_cmd)

        current_ref = RefStatus()
        current_ref.ref_pose = list(desired_pose)
        current_ref.ref_vel = list(desired_vel)
        current_ref.timestamp = time.time() - self.start_time
        current_ref.stop = stop #仿真结束标志位
        self.ref_pub.publish(current_ref) #参考位置，速度
        
    
    def status_publish(self):
        current_status = RobotStatus()
        current_status.ft_vector = self.world_force_filtered.flatten()
        current_status.pos_vector = self.eef_pos
        current_status.rotation_matrix = self.eef_rotm.flatten()  # 展平为1D数组
        current_status.vel_vector = self.eef_vel.flatten()
        self.status_pub.publish(current_status)

    def step(self, action):
        # step function for RL
        # desired_vel, desired_kp = self.process_action(action)  # self.process_action(action)

        desired_pose = action
        desired_pos = desired_pose[:3]
        desired_rotm = trans_quat.quat2mat(desired_pose[3:])

        link6_pos, link6_rotm = self.get_link6_pose_(desired_pos, desired_rotm)

        q_target = self.kdl.ik(self.d.qpos[self.joint_6_id - 5: self.joint_6_id + 1], link6_pos,
                                     link6_rotm)
        target_pos = q_target

        force = np.array([0, 0, 0, 0, 0, 10])
        peg_id = mujoco.mj_name2id(self.m, mujoco.mjtObj.mjOBJ_BODY, "peg")
        peg_quat = self.d.xquat[peg_id]


        # 准备一个 3x3 矩阵来存储旋转矩阵
        rot_mat = np.zeros(9)
        # 从四元数计算旋转矩阵
        mujoco.mju_quat2Mat(rot_mat, peg_quat)
        # 将 1D 旋转矩阵转换为 3x3 矩阵
        rot_mat = rot_mat.reshape((3, 3))
        # 将局部坐标系的力矩转换到世界坐标系
        local_torque = force[3:6]
        global_torque = np.dot(rot_mat, local_torque)
        # 合并到力和力矩数组
        force = np.concatenate([force[:3], global_torque])
        self.d.xfrc_applied[peg_id, :] = force
        # keep the same action for a short time
        for i in range(60):
            done = False
            self.set_joint_pos(target_pos)
            self.sim_step()
    

    def sim_step(self):
        # apply computed torque control
        # self.computed_torque_control()
        self.computed_torque_control_robopal()
        # self.pd_torque_control()
        mujoco.mj_step(self.m, self.d)
        if self.render:
            self.viewer.sync()
        # update robot state
        self.update_pose_vel()
        self.get_force_sensor_data()
 
    def reset(self):
        # q_target = np.array([-np.pi / 2, np.pi / 3, np.pi * 2 / 3, np.pi / 2, -np.pi / 2, np.pi / 2])


        desired_pos = np.array([0, 0.37, 0.08])

        # 定义绕 x 轴旋转 90 度（角度单位为度）
        rot = R.from_euler('z', 90, degrees=True)
        # 获取旋转矩阵
        desired_rotm = rot.as_matrix()
        
 
        link6_linear, link6_angular = self.get_link6_pose_(desired_pos, desired_rotm)
        q_target = self.kdl.ik(self.d.qpos[self.joint_6_id - 5: self.joint_6_id + 1], link6_linear,
                                     link6_angular)
        

        self.d.qpos[self.joint_6_id - 5:self.joint_6_id + 1] = q_target.copy()
        mujoco.mj_step(self.m, self.d)
        self.viewer.sync()

        r2, p2 = self.kdl.fk(q_target.copy())
        r2 = np.array(r2)

        quat_p2 = trans_quat.mat2quat(np.array(p2))
        link6_pose_ = np.concatenate([r2, quat_p2])
     
        eef_pos, eef_rotm = self.get_eef_pose_(link6_pose_)

        return eef_pos, eef_rotm

    def set_reference_traj(self, ref_joint, ref_vel, ref_acc):
        assert (
                ref_joint.shape == (6,) and ref_vel.shape == (6,) and ref_acc.shape == (6,)
        )
        self.ref_joint = ref_joint
        self.ref_vel = ref_vel
        self.ref_acc = ref_acc


    def set_joint_pos(self, target_pos):
        T = 1 / self.HZ
        target_pos = target_pos.copy()

        target_vel = (target_pos - self.joint_pos) / T
        target_acc = (target_vel - self.joint_vel) / T
        self.set_reference_traj(target_pos, target_vel, target_acc)

    def pd_torque_control(self):

        tau_right = self.joint_kp * (self.ref_joint[6:] - self.right_joint_pos) + self.joint_kd * (self.ref_vel[6:] - self.right_joint_vel)

        self.d.ctrl[self.actuator_id - 5: self.actuator_id + 1] = np.clip(tau_right, -100, 100)

        self.d.ctrl[self.screw_shaft_id] = 0  # gripper_pose should be defined or passed as an argument

    def computed_torque_control_robopal(self):
        M = np.zeros((self.m.nv, self.m.nv))
        mujoco.mj_fullM(self.m, M, self.d.qM)

        M_ = M[self.joint_6_id - 5: self.joint_6_id + 1, self.joint_6_id - 5: self.joint_6_id + 1]
        c_g_ = self.d.qfrc_bias[self.joint_6_id - 5 : self.joint_6_id + 1]

        # 也可以称之为是一种前馈+反馈控制器
        acc_desire_right = self.joint_kp * (self.ref_joint - self.joint_pos) + self.joint_kd * ( -self.joint_vel)
        tau_right = np.dot(M_, acc_desire_right) + c_g_

        self.d.ctrl[self.actuator_id - 5: self.actuator_id + 1] = np.clip(tau_right, -1000, 1000)
        # print('--',self.d.ctrl[self.actuator_id - 5: self.actuator_id + 1])

        self.d.ctrl[self.screw_shaft_id] = 0  # gripper_pose should be defined or passed as an argument


    def computed_torque_control(self):
        # Assuming self.m and self.d are equivalent to m and d in the C++ code
        # 前馈 - 反馈控制（feedforward and feedback control）
        # The low-level position/velocity controller is achieved via a Positional-Integral (PI) control law with feed-forward terms to cancel gravity and friction
        # Compute inverse dynamics forces
        mujoco.mj_rne(self.m, self.d, 0, self.d.qfrc_inverse)
        for i in range(self.m.nv):
            self.d.qfrc_inverse[i] += (self.m.dof_armature[i] * self.d.qacc[i] -
                                       self.d.qfrc_passive[i] -
                                       self.d.qfrc_constraint[i])

        # Error and error derivative
        e = self.joint_pos - self.ref_joint[6:]
        e_dot = self.joint_vel
        # right_e = self.d.qpos[self.right_joint_id - 5 : self.right_joint_id + 1] - self.ref_joint[6:]  # ref_joint should be defined or passed as an argument
        # right_e_dot = self.d.qvel[self.right_joint_id - 5 : self.right_joint_id + 1] - self.ref_vel[6:]  # ref_vel should be defined or passed as an argument

        # Control law components
        kve_dot = np.multiply(self.joint_kd, e_dot)  # kv should be defined or passed as an argument
        kpe = np.multiply(self.joint_kp, e)  # kp should be defined or passed as an argument
        # right_inertial_pd = self.ref_acc[6:] - right_kve_dot - right_kpe  # ref_acc should be defined or passed as an argument
        inertial_pd = - kve_dot - kpe
        # #在上述约束力计算中，self.d.qfrc_constraint[i] 可能包含了来自环境的外部力 ( \tau_{\text{env}} ) —— 比如接触反作用力等。
        # 最终通过控制器施加到机器人关节上的力矩是将环境力和期望的控制力矩叠加的结果，其旨在驱动机器人执行期望的运动，同时考虑与环境的交互。

        # Compute full inertia matrix
        M = np.zeros((self.m.nv, self.m.nv))
        mujoco.mj_fullM(self.m, M, self.d.qM)
        M_right = M[self.joint_6_id - 5: self.joint_6_id + 1, self.joint_6_id - 5: self.joint_6_id + 1]
        # M_robot = M[:self.m.nu, :self.m.nu]  # Assuming self.m.nu is the number of actuators

        # Compute the control torques
        inertial_torque = np.dot(M_right, inertial_pd)

        # Apply control and inverse dynamics torques
        self.d.ctrl[self.actuator_id - 5: self.actuator_id + 1] = np.clip(inertial_torque +
                                                                                    self.d.qfrc_inverse[self.joint_6_id - 5: self.joint_6_id + 1], -20, 20)

        self.d.ctrl[self.screw_shaft_id] = 0  # gripper_pose should be defined or passed as an argument
 
    def process_action(self, action):
        # 这段代码用于在某些范围内，通常是 -1 到 1 之间的标准化值）重新映射到一个特定的速度范围（即 self.action_vel_high 和 self.action_vel_low 之间），以便将其应用于机械臂的关节。
        # 这实质上是一个线性变换，它将智能体的输出（假设是一个在 [-1, 1] 之间的控制信号）转换为实际的关节速度命令。这个转换保证了智能体的输出能够映射到环境能接受的动作空间范围内。
        # Normalize actions
        desired_joint = np.clip(action[:6], -1, 1)

        desired_joint = (self.action_pos_high + self.action_pos_low) / 2 + np.multiply(desired_joint, (
                    self.action_pos_high - self.action_pos_low) / 2)
        return desired_joint

def main():
    
    print("当前 Python 解释器路径:", sys.executable)

    #轨迹离线生成
    # t0 = 0.0
    # traj_length = 0.35  # 轨迹长度：5 米
    # speed = 0.01  # 速度：0.01 米/秒
    # dt = 0.008  # 控制频率：125 Hz
    # position_sequence = np.zeros((1, 3))
    # orientation_sequence = np.array([[1, 0, 0, 0]])
    env = Dual_arm_env()

    # 声明参数并提供默认值
    env.node.declare_parameter('t0', 0.0)
    env.node.declare_parameter('traj_length', 0.4)
    env.node.declare_parameter('speed', 0.01)
    env.node.declare_parameter('dt', 0.008)
    env.node.declare_parameter('position_sequence', [0.0, 0.0, 0.0])
    env.node.declare_parameter('orientation_sequence', [1.0, 0.0, 0.0, 0.0])

    t0 =                   env.node.get_parameter('t0').value
    traj_length =          env.node.get_parameter('traj_length').value
    speed =                env.node.get_parameter('speed').value
    dt =                   env.node.get_parameter('dt').value
    position_sequence =    np.array([env.node.get_parameter('position_sequence').value])
    orientation_sequence = np.array([env.node.get_parameter('orientation_sequence').value])

    # 轨迹生成
    trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = (
        traj.generate_straight_trajectory(traj_length, dt, speed, position_sequence, orientation_sequence)) #生成x方向的直线轨迹

    traj_1 = np.hstack((trajectory_positions[:, [0]], trajectory_velocities[:, [0]]))
    traj_1 = np.hstack((traj_1, np.zeros((len(trajectory_positions), 1))))
    traj_2 = np.hstack((trajectory_positions[:, [1]], trajectory_velocities[:, [1]]))
    traj_2 = np.hstack((traj_2, np.zeros((len(trajectory_positions), 1))))
    traj_3 = np.hstack((trajectory_positions[:, [2]], trajectory_velocities[:, [2]]))
    traj_3 = np.hstack((traj_3, np.zeros((len(trajectory_positions), 1))))

    traj_all =  np.hstack((traj_1, traj_2, traj_3)) # x * 9

    action_pose = env.start_pose_quat.copy()  #当前eef的位姿（7，1), 设位初始期望位姿
    action_vel = np.zeros(6) #期望速度
    stop = 0

    t = 0
    # 仿真启动, 仿真步长为0.008s，每个导纳周期更新一次
    for _ in range(100000):
        # print('************************************')
        rclpy.spin_once(env.node, timeout_sec=0.0)
        t = t + 1
        start = time.time()
        start_time = env.node.get_clock().now().nanoseconds * 1e-9

        if (t < len(traj_all)):
            incre_pos = np.array([traj_all[t, 0], traj_all[t, 3], traj_all[t, 6]])
            action_pose[:3] = env.start_pos + env.start_rotm @ incre_pos
            incre_vel = np.array([traj_all[t, 1], traj_all[t, 4], traj_all[t, 7]])
            action_vel[:3] = env.start_rotm @ incre_vel
            stop=0
        else:
            incre_pos = np.array([traj_all[-1, 0], traj_all[-1, 3], traj_all[-1, 6]])
            action_pose[:3] = env.start_pos + env.start_rotm @ incre_pos
            incre_vel = np.array([traj_all[-1, 1], traj_all[-1, 4], traj_all[-1, 7]])
            action_vel[:3] = env.start_rotm @ incre_vel
            stop=1

        env.admittance_step_test(action_pose, action_vel, stop)
        end_time = env.node.get_clock().now().nanoseconds * 1e-9
        # print("sim time =", end_time - start_time) #稳定耗时12ms
        # print("input=", env.adm_d)
        # print('------------------------------------')

if __name__ == '__main__':
    main()
