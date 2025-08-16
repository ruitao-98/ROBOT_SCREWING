from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, OpaqueFunction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, TextSubstitution
import os
import shutil

def ensure_directory(context, *args, **kwargs):
    # 获取保存路径并确保目录存在
    save_path = context.launch_configurations['save_path']
    os.makedirs(save_path, exist_ok=True)
    return []

def clear_existing_bag(context, *args, **kwargs):
    save_path = context.launch_configurations['save_path']
    bag_number = context.launch_configurations['bag_number']
    bag_folder = os.path.join(save_path, f"santong_{bag_number}")
    if os.path.exists(bag_folder):
        shutil.rmtree(bag_folder)  # Delete existing bag folder
    return []

def generate_launch_description():
    # 声明命令行参数
    bag_number = LaunchConfiguration('bag_number')
    save_path = LaunchConfiguration('save_path')  # 添加 save_path 的 LaunchConfiguration
    para_name = LaunchConfiguration('para_name')
    
    # 动态生成保存路径（与 src 同级的 rosbag_record/with_mpc）
    # src_dir = os.path.abspath("/home/yanji/robot_screwing")
    # save_path = os.path.join(src_dir, 'rosbag_record', 'with_mpc')

    return LaunchDescription([
        # 命令行参数：bag 文件编号
        DeclareLaunchArgument(
            'bag_number',
            default_value='01',
            description='Number for bag file name (e.g., 01 for santong_01.bag)'
        ),
        DeclareLaunchArgument(
            'save_path',
            default_value='/home/yanji/rosbag_record/with_mpc',
            description='Directory to save the rosbag file'
        ),
        DeclareLaunchArgument(
            'para_name',
            default_value='santong_',
            description='Prefix for bag file name (e.g., santong_ for santong_01.bag)'
        ),
        # 原节点：task_control_screw
        Node(
            package='screw_robot_control',
            executable='task_control_screw',
            name='task_control_screw',
            output='screen',
            emulate_tty=True
        ),
        # 新节点：mpc_node_pose
        # Node(
        #     package='mj_sim',
        #     executable='pose_mpc_node',
        #     name='pose_mpc_node',
        #     output='screen',
        #     emulate_tty=True
        # ),
        # 确保保存路径存在
        OpaqueFunction(function=ensure_directory),
        # 删除现有的 bag 文件夹
        OpaqueFunction(function=clear_existing_bag),
        # ros2 bag record
        ExecuteProcess(
            cmd=[
                'ros2', 'bag', 'record',
                '/cmd_status', '/rob_status', '/ref_status', '/current_p',
                # '-o', [save_path, '/', TextSubstitution(text='para_a_'), bag_number]
                '-o', [save_path, '/', para_name, bag_number]
            ],
            output='screen'
        ),
    ])

#ros2 launch screw_robot_control server_mpc.launch.py para_name:=santong_ bag_number:=01