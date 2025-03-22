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
from mj_sim.mpc_optimizer import Mpc_Opti, predict_next_state
import trajectory_planner as traj
import numpy as np
from robot_msgs.msg import ControlCommand
from robot_msgs.msg import RobotStatus 
from robot_msgs.msg import RefStatus
import threading
from std_srvs.srv import Trigger
import time
from robot_msgs.srv import StartPose
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import safe_mknode_recursive, jsonify, get_data_dir_and_file
import pandas as pd
import copy
from config.configuration import RecordingOptions, SimpleSimConfig


class Data_Recorder(Node):
    def __init__(self):
        super().__init__("data_recorder")  # 初始化节点，命名为 'mpc_node'
        self.mpc_predict = Mpc_Opti()

        self.eef_rotm = np.zeros((3,3))
        self.eef_pos = np.zeros(3)
        self.eef_vel = np.zeros(6)
        self.world_force = np.zeros(6)
        self.ref_pose = np.zeros(7)
        self.ref_vel = np.zeros(6)
        self.timestamp = 0.0
        self.stop = 0

        self.adm_k = 1400 * np.array([1, 1, 1, 1, 1, 1])  
        self.adm_m = 2 * np.array([1, 1, 1, 1, 1, 1])
        self.adm_d = 4 * np.sqrt(np.multiply(self.adm_k,
                                              self.adm_m))
        recording_options = RecordingOptions.recording_options
        simulation_options = SimpleSimConfig.simulation_disturbances

        self.last_timestamp = 0.0  # 上次处理的时间戳
        
        self.blank_recording_dict = self.make_record_dict() # 初始化空字典
        self.rec_dict, self.rec_file = self.get_record_file_and_dir(self.blank_recording_dict, recording_options, simulation_options)

        self.status_sub = self.create_subscription(RobotStatus, "rob_status", self.status_callback, 1)
        self.ref_sub = self.create_subscription(RefStatus, "ref_status", self.ref_callback, 1)
        self.command_sub = self.create_subscription(ControlCommand, "cmd_status", self.command_callback, 1)

    
    def status_callback(self, msg):
        self.world_force = np.array(msg.ft_vector)
        self.eef_pos = np.array(msg.pos_vector)
        self.eef_rotm = np.array(msg.rotation_matrix).reshape(3,3)
        self.eef_vel = np.array(msg.vel_vector)
    
    def command_callback(self, msg):
        self.adm_k = np.array(msg.k, dtype=np.float64) 
        self.adm_d = np.array(msg.d, dtype=np.float64)
    
    def ref_callback(self, msg):
        self.ref_pose = np.array(msg.ref_pose, dtype=np.float64)
        self.ref_vel = np.array(msg.ref_vel, dtype=np.float64)
        self.timestamp = msg.timestamp
        self.stop = msg.stop
    
    ####################
    def get_record_file_and_dir(self, record_dict_template, recording_options, simulation_setup, overwrite=False): #更改configuration， simulation_setup，才能创建新文件
        dataset_name = recording_options["dataset_name"]
        training_split = recording_options["training_split"]

        # Directory and file name for data recording
        rec_file_dir, rec_file_name = get_data_dir_and_file(dataset_name, training_split, simulation_setup)
        print(rec_file_name)

        overwritten = safe_mknode_recursive(rec_file_dir, rec_file_name, overwrite=overwrite)
        print(overwritten)
        print(overwrite)
        rec_dict = copy.deepcopy(record_dict_template)
        rec_file = os.path.join(rec_file_dir, rec_file_name)
        if overwrite or (not overwritten):
            for key in rec_dict.keys():
                rec_dict[key] = jsonify(rec_dict[key])
            print('---')
            df = pd.DataFrame(rec_dict)
            df.to_csv(rec_file, index=False, header=True)

            rec_dict = copy.deepcopy(record_dict_template)

        return rec_dict, rec_file

    def make_record_dict(self):
        blank_recording_dict = {
            "state_in_pose": np.zeros((0, 3+9)),    # 位置+旋转矩阵，第一步初始状态
            "state_in_vel": np.zeros((0, 6)),       # 速度
            "state_in_force": np.zeros((0, 6)),     # 力/力矩
            "state_ref_pose": np.zeros((0, 7)),     # 位置+四元数
            "state_ref_vel": np.zeros((0, 6)),      # 6维度速度
            "error": np.zeros((0, 3*3)),            # 3 * (x-x_r, x_dot-x_dot_r, f-f_r) 实际状态（state_out）与预测状态（state_pred）之间的误差
            "input_in": np.zeros((0, 6+6)),         # (k,d)*6维，当前状态情况下的输入
            "state_pred": np.zeros((0, 3*3)),       # 基于理论动力学模型预测的状态， 3 * (x, x_dot, f)
            "timestamp": np.zeros((0, 1)),          # 时间戳
        }
        return blank_recording_dict

    def check_out_data(self, rec_dict, state_final, x_pred, w_opt, dt):
        rec_dict["dt"] = np.append(rec_dict["dt"], dt)
        rec_dict["input_in"] = np.append(rec_dict["input_in"], w_opt[np.newaxis, :4], axis=0)
        rec_dict["state_out"] = np.append(rec_dict["state_out"], state_final, 0)

        if x_pred is not None:
            err = state_final - x_pred
            rec_dict["error"] = np.append(rec_dict["error"], err, axis=0)
            rec_dict["state_pred"] = np.append(rec_dict["state_pred"], x_pred[np.newaxis, :], axis=0)

        return rec_dict
    
    #############

    def process_data(self):
        if not self.stop:
            # print(self.timestamp)
            if self.timestamp != self.last_timestamp:
                print('--update--')
                state_in_pose = np.concatenate((self.eef_pos, self.eef_rotm.flatten())).reshape(1, 12)
                self.rec_dict["state_in_pose"] = np.append(self.rec_dict["state_in_pose"], state_in_pose, axis=0)
                self.rec_dict["state_in_vel"] = np.append(self.rec_dict["state_in_vel"], self.eef_vel.reshape(1, 6), axis=0)
                self.rec_dict["state_in_force"] = np.append(self.rec_dict["state_in_force"], self.world_force.reshape(1, 6), axis=0)
                self.rec_dict["state_ref_pose"] = np.append(self.rec_dict["state_ref_pose"], self.ref_pose.reshape(1, 7), axis=0)
                self.rec_dict["state_ref_vel"] = np.append(self.rec_dict["state_ref_vel"], self.ref_vel.reshape(1, 6), axis=0)

                error_x = np.array([self.eef_pos[0]-self.ref_pose[0], self.eef_vel[0]-self.ref_vel[0], self.world_force[0]-0])
                error_y = np.array([self.eef_pos[1]-self.ref_pose[1], self.eef_vel[1]-self.ref_vel[2], self.world_force[1]-0])
                error_z = np.array([self.eef_pos[2]-self.ref_pose[2], self.eef_vel[2]-self.ref_vel[2], self.world_force[2]-0])
                error_xyz = np.concatenate((error_x, error_y, error_z)).reshape(1, 9)
                self.rec_dict["error"] = np.append(self.rec_dict["error"], error_xyz, axis=0)

                input = np.concatenate((self.adm_k, self.adm_d)).reshape(1, 12)
                self.rec_dict["input_in"] = np.append(self.rec_dict["input_in"], input, axis=0)

                Next_State = np.zeros((1, 9))
                for i in range(3):
                    _state = np.array([self.eef_pos[i], self.eef_vel[i], self.world_force[i]])      # [x, x_dot, f_x]
                    _ref = np.array([self.ref_pose[i], self.ref_vel[i], 0.0])          # [x_r, x_dot_r, f_xr]
                    _input = np.array([-self.adm_k[i]/self.adm_m[i], -self.adm_d[i]/self.adm_m[i], 1/self.adm_m[i]])   # [u_0, u_1, u_2]
                    next_state = predict_next_state(self.mpc_predict, _state, _ref, _input)
                    Next_State[0, i*3:i*3 + 3] = next_state

                self.rec_dict["state_pred"] = np.append(self.rec_dict["state_pred"], Next_State, axis=0)

                self.rec_dict["timestamp"] = np.append(self.rec_dict["timestamp"], [[self.timestamp]], axis=0)

                self.last_timestamp = self.timestamp
        else:
            print('stop')
            for key in self.rec_dict.keys():
                self.rec_dict[key] = jsonify(self.rec_dict[key])

            df = pd.DataFrame(self.rec_dict)
            df.to_csv(self.rec_file, index=True, mode='a', header=False)

def main():
    rclpy.init() 
    data_re = Data_Recorder()
    
    # 主循环
    try:
        while rclpy.ok():
            
            # 处理一次消息队列中的回调
            rclpy.spin_once(data_re, timeout_sec=0.005)
            
            # 在回调处理完后，集中处理属性并存储
            data_re.process_data() 
            if data_re.stop:
                break

    except KeyboardInterrupt:
        data_re.get_logger().info("Shutting down data recorder...")
        data_re.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

    



