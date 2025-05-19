from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='screw_robot_control',
            executable='right_arm_control',
            name='right_arm_control',
            output='screen',
            emulate_tty=True
        ),
        Node(
            package='screw_robot_control',
            executable='task_control_screw',
            name='task_control_screw',
            output='screen',
            emulate_tty=True
        )
    ])