import numpy as np
import matplotlib.pyplot as plt



def generate_straight_trajectory(length, control_dt, speed, position_sequence, orientation_sequence):
    """
    生成沿着z轴正方向的直线轨迹，保持姿态不变。

    :param length: 轨迹的长度 (m)
    :param speed: 速度 (m/s)
    :param control_dt: 控制周期 (s)
    :param position_sequence: 初始位置序列，包含 xyz (例如：[[x0, y0, z0]])
    :param orientation_sequence: 初始姿态序列，包含 quaternion (例如：[[w, x, y, z]])

    :return: 轨迹位置和姿态序列
    """
    # 计算轨迹的总时间
    total_time = length / speed
    # print(speed)

    # 计算轨迹点数
    num_points = int(total_time / control_dt)

    # 初始化轨迹数组
    trajectory_positions = np.zeros((num_points, 3))  # 位置 [x, y, z]
    trajectory_orientations = np.zeros((num_points, 4))  # 姿态 [w, x, y, z]
    trajectory_velocities = np.zeros((num_points, 3))  # 线速度 [vx, vy, vz]
    trajectory_angular_velocities = np.zeros((num_points, 3))  # 角速度 [wx, wy, wz]

    # 提取初始位置和姿态
    start_position = position_sequence[0]
    start_orientation = orientation_sequence[0]


    # 在 z 轴上沿正方向生成轨迹
    for i in range(num_points):
        # 位置更新
        x_position = start_position[0] + i * (speed * control_dt)
        trajectory_positions[i, :] = [x_position, start_position[1], start_position[2]]

        # 姿态保持不变
        trajectory_orientations[i, :] = start_orientation

        trajectory_velocities[i, :] = [speed, 0, 0]

        # 姿态不发生变化，所以角速度为零
        trajectory_angular_velocities[i, :] = [0, 0, 0]


    return trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities


# 可视化生成的轨迹
def plot_trajectory(trajectory_positions):
    """
    可视化生成的轨迹
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(trajectory_positions[:, 0], trajectory_positions[:, 1], trajectory_positions[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title("Straight Line Trajectory")
    plt.show()




if __name__ == "__main__":
    traj_length = 0.35  # 轨迹长度：5 米
    speed = 0.01  # 速度：1 米/秒
    dt = 0.008  # 控制频率：125 Hz
    position_sequence = np.zeros((1, 3))
    print(position_sequence)
    orientation_sequence = np.array([[1, 0, 0, 0]])

    trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = (
        generate_straight_trajectory(traj_length, dt, speed, position_sequence, orientation_sequence))
    print(trajectory_positions)
    c_p = np.concatenate((trajectory_positions[3, [0, 2]], trajectory_velocities[3, [0, 2]]))
    c_p = np.concatenate((c_p, np.array([0, 0])))
    print(c_p)
    print( trajectory_positions[-1, 2])
    print(len(trajectory_positions))
    print(np.zeros((len(trajectory_positions), 2)))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    xx = np.array(trajectory_positions)
    # ax.plot(xx[0,:], xx[1,:])
    ax.plot(trajectory_positions[:, 0], trajectory_positions[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    plt.title("Straight Line Trajectory")
    plt.show()


    plot_trajectory(trajectory_positions)
