from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # 定义启动参数
    t0 = LaunchConfiguration('t0', default='0.0')
    traj_length = LaunchConfiguration('traj_length', default='0.35')
    speed = LaunchConfiguration('speed', default='0.01')
    dt = LaunchConfiguration('dt', default='0.008')
    position_sequence = LaunchConfiguration('position_sequence', default='[0.0, 0.0, 0.0]')
    orientation_sequence = LaunchConfiguration('orientation_sequence', default='[1.0, 0.0, 0.0, 0.0]')

    # 定义节点
    robot_sim_node = Node(
        package='mj_sim',
        namespace='',
        executable='robot_sim_env',  # 改为 executable，值是 entry_points 中的名称
        name='robot_sim_env',
        output='screen',  # 去掉 exec_name，它不是必需的
        parameters=[
            {'t0': t0},
            {'traj_length': traj_length},
            {'speed': speed},
            {'dt': dt},
            {'position_sequence': position_sequence},
            {'orientation_sequence': orientation_sequence}
        ]
    )

    mpc_node = Node(
        package='mj_sim',
        namespace='',
        executable='mpc_node',  # 改为 executable，值是 entry_points 中的名称
        name='mpc_node',
        output='screen',  # 去掉 exec_name
        parameters=[
            {'t0': t0},
            {'traj_length': traj_length},
            {'speed': speed},
            {'dt': dt},
            {'position_sequence': position_sequence},
            {'orientation_sequence': orientation_sequence}
        ]
    )

    return LaunchDescription([
        # 声明启动参数
        DeclareLaunchArgument('t0', default_value='0.0', description='Initial time'),
        DeclareLaunchArgument('traj_length', default_value='0.35', description='Trajectory length in meters'),
        DeclareLaunchArgument('speed', default_value='0.01', description='Speed in meters/second'),
        DeclareLaunchArgument('dt', default_value='0.008', description='Control frequency timestep'),
        DeclareLaunchArgument('position_sequence', default_value='[0.0, 0.0, 0.0]', description='Position sequence as flat list'),
        DeclareLaunchArgument('orientation_sequence', default_value='[1.0, 0.0, 0.0, 0.0]', description='Orientation sequence as flat list (quaternion)'),

        # 先启动 robot_sim_env（服务端）
        robot_sim_node,

        mpc_node,

        # 延迟 1 秒启动 mpc_node（客户端）
        # TimerAction(
        #     period=1.0,
        #     actions=[mpc_node]
        # ),
    ])