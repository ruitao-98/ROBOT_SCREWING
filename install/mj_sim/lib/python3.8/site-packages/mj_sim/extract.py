#! /home/yanji/anaconda3/envs/screwrobot/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
# print("当前 Python 解释器路径:", sys.executable)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print("当前 sys.path:", sys.path)  # 调试用
sys.path.append(f'/home/yanji/anaconda3/envs/screwrobot/lib/python3.8/site-packages')
import rosbag_py
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message
import csv


def parse_rosbag(bag_path, output_dir):
    # Initialize storage options and reader
    storage_options = rosbag_py.StorageOptions(uri=bag_path, storage_id='sqlite3')
    converter_options = rosbag_py.ConverterOptions(
        input_serialization_format='cdr',
        output_serialization_format='cdr'
    )
    reader = rosbag_py.SequentialReader()
    reader.open(storage_options, converter_options)

    # Define topics and message types
    topics = {
        '/cmd_status': 'your_package/msg/CmdStatus',
        '/rob_status': 'your_package/msg/RobStatus'
    }

    # Create output files
    os.makedirs(output_dir, exist_ok=True)
    txt_file_cmd = os.path.join(output_dir, 'cmd_status.txt')
    txt_file_rob = os.path.join(output_dir, 'rob_status.txt')
    csv_file_cmd = os.path.join(output_dir, 'cmd_status.csv')
    csv_file_rob = os.path.join(output_dir, 'rob_status.csv')

    # Open TXT and CSV files
    with open(txt_file_cmd, 'w') as f_cmd, open(txt_file_rob, 'w') as f_rob, \
         open(csv_file_cmd, 'w', newline='') as cf_cmd, open(csv_file_rob, 'w', newline='') as cf_rob:
        
        # CSV writers
        csv_writer_cmd = csv.writer(cf_cmd)
        csv_writer_rob = csv.writer(cf_rob)
        
        # Write CSV headers
        csv_writer_cmd.writerow(['timestamp', 'k[0]', 'k[1]', 'k[2]', 'k[3]', 'k[4]', 'k[5]',
                                 'd[0]', 'd[1]', 'd[2]', 'd[3]', 'd[4]', 'd[5]'])
        csv_writer_rob.writerow(['timestamp', 
                                 'ft_vector[0]', 'ft_vector[1]', 'ft_vector[2]', 'ft_vector[3]', 'ft_vector[4]', 'ft_vector[5]',
                                 'pos_vector[0]', 'pos_vector[1]', 'pos_vector[2]',
                                 'rotation_matrix[0]', 'rotation_matrix[1]', 'rotation_matrix[2]',
                                 'rotation_matrix[3]', 'rotation_matrix[4]', 'rotation_matrix[5]',
                                 'rotation_matrix[6]', 'rotation_matrix[7]', 'rotation_matrix[8]',
                                 'vel_vector[0]', 'vel_vector[1]', 'vel_vector[2]', 'vel_vector[3]', 'vel_vector[4]', 'vel_vector[5]'])

        # Read messages
        while reader.has_next():
            (topic, data, t) = reader.read_next()
            if topic not in topics:
                continue

            # Convert timestamp to seconds
            timestamp = t / 1e9  # Convert nanoseconds to seconds

            # Deserialize message
            msg_type = get_message(topics[topic])
            msg = deserialize_message(data, msg_type)

            if topic == '/cmd_status':
                # Write to TXT
                f_cmd.write(f"Timestamp: {timestamp:.6f}\n")
                f_cmd.write(f"k: {msg.k}\n")
                f_cmd.write(f"d: {msg.d}\n\n")
                # Write to CSV
                csv_writer_cmd.writerow([timestamp] + list(msg.k) + list(msg.d))
            
            elif topic == '/rob_status':
                # Write to TXT
                f_rob.write(f"Timestamp: {timestamp:.6f}\n")
                f_rob.write(f"ft_vector: {msg.ft_vector}\n")
                f_rob.write(f"pos_vector: {msg.pos_vector}\n")
                f_rob.write(f"rotation_matrix: {msg.rotation_matrix}\n")
                f_rob.write(f"vel_vector: {msg.vel_vector}\n\n")
                # Write to CSV
                csv_writer_rob.writerow([timestamp] + list(msg.ft_vector) + list(msg.pos_vector) +
                                       list(msg.rotation_matrix) + list(msg.vel_vector))

    print(f"Data saved to {output_dir}")

if __name__ == '__main__':
    bag_path = '/home/yanji/rosbag_record/mpc_track/santong_01'
    output_dir = '/home/yanji/rosbag_record/mpc_track_convert'
    parse_rosbag(bag_path, output_dir)