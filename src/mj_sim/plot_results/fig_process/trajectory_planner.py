import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
import transforms3d.quaternions as trans_quat

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

def online_generate_straight_trajectory(num_points, control_dt, speed, position, orientation, present_position):
 
    # 初始化轨迹数组
    trajectory_positions = np.zeros((num_points + 1, 3))  # 位置 [x, y, z]
    trajectory_orientations = np.zeros((num_points + 1, 4))  # 姿态 [w, x, y, z]
    trajectory_velocities = np.zeros((num_points + 1, 3))  # 线速度 [vx, vy, vz]
    trajectory_angular_velocities = np.zeros((num_points + 1, 3))  # 角速度 [wx, wy, wz]

    # 提取初始位置和姿态
    start_position = position
    start_orientation = orientation
    # 末端坐标系的z轴负方向单位向量
    z_negative = np.array([0, 0, -1])
    # 转换到世界坐标系的方向向量
    direction = start_orientation @ z_negative
    quaternion = trans_quat.mat2quat(start_orientation)

    # 在 z 轴上沿正方向生成轨迹
    for i in range(num_points + 1):
        # 距离（速度 × 时间）
        distance = i * speed * control_dt
        # 位置更新：
        # x: 初始x坐标
        # y: 初始y坐标
        # z: 当前z坐标 + 沿z负方向的位移
        trajectory_positions[i, :] = np.array([
            start_position[0],                       # 初始x
            start_position[1],                       # 初始y
            present_position[2] + distance * direction[2]  # 当前z + z方向位移
        ]) + np.array([distance * direction[0], distance * direction[1], 0])

        # trajectory_positions[i, :] = start_position + distance * direction
        # 姿态保持不变
        trajectory_orientations[i, :] = quaternion
        # 线速度：速度 × 方向
        trajectory_velocities[i, :] = speed * direction
        # 姿态不发生变化，角速度为零
        trajectory_angular_velocities[i, :] = [0, 0, 0]
 

    return trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities


def generate_rectangular_trajectory(length, control_dt, speed, position_sequence, orientation_sequence):
    """
    生成XY平面上的矩形轨迹，保持姿态不变。

    :param length: 矩形边长 (m)
    :param speed: 速度 (m/s)
    :param control_dt: 控制周期 (s)
    :param position_sequence: 初始位置序列，包含 xyz (例如：[[x0, y0, z0]])
    :param orientation_sequence: 初始姿态序列，包含 quaternion (例如：[[w, x, y, z]])

    :return: 轨迹位置、姿态、线速度和角速度序列
    """
    # 计算每个边的总时间
    time_per_side = length / speed
    # 每个边的点数
    points_per_side = int(time_per_side / control_dt)
    # 总点数（4条边）
    num_points = points_per_side * 4

    # 初始化轨迹数组
    trajectory_positions = np.zeros((num_points, 3))  # 位置 [x, y, z]
    trajectory_orientations = np.zeros((num_points, 4))  # 姿态 [w, x, y, z]
    trajectory_velocities = np.zeros((num_points, 3))  # 线速度 [vx, vy, vz]
    trajectory_angular_velocities = np.zeros((num_points, 3))  # 角速度 [wx, wy, wz]

    # 提取初始位置和姿态
    start_position = position_sequence[0]
    start_orientation = orientation_sequence[0]

    # 定义矩形的四个阶段（沿X正方向、Y正方向、X负方向、Y负方向）
    for i in range(num_points):
        # 当前时间
        current_time = i * control_dt
        # 确定当前所在的边
        side = i // points_per_side
        side_progress = (i % points_per_side) * control_dt * speed

        if side == 0:  # 沿X正方向
            trajectory_positions[i, :] = [start_position[0] + side_progress, start_position[1], start_position[2]]
            trajectory_velocities[i, :] = [speed, 0, 0]
        elif side == 1:  # 沿Y正方向
            trajectory_positions[i, :] = [start_position[0] + length, start_position[1] + side_progress, start_position[2]]
            trajectory_velocities[i, :] = [0, speed, 0]
        elif side == 2:  # 沿X负方向
            trajectory_positions[i, :] = [start_position[0] + length - side_progress, start_position[1] + length, start_position[2]]
            trajectory_velocities[i, :] = [-speed, 0, 0]
        else:  # 沿Y负方向
            trajectory_positions[i, :] = [start_position[0], start_position[1] + length - side_progress, start_position[2]]
            trajectory_velocities[i, :] = [0, -speed, 0]

        # 姿态保持不变
        trajectory_orientations[i, :] = start_orientation
        # 角速度为零
        trajectory_angular_velocities[i, :] = [0, 0, 0]

    return trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities


def generate_triangular_trajectory(length, control_dt, speed, position_sequence, orientation_sequence):
    """
    生成XY平面上的等边三角形轨迹，保持姿态不变。

    :param length: 三角形边长 (m)
    :param speed: 速度 (m/s)
    :param control_dt: 控制周期 (s)
    :param position_sequence: 初始位置序列，包含 xyz (例如：[[x0, y0, z0]])
    :param orientation_sequence: 初始姿态序列，包含 quaternion (例如：[[w, x, y, z]])

    :return: 轨迹位置、姿态、线速度和角速度序列
    """
        # 计算每个边的总时间
    time_per_side = length / speed
    # 每个边的点数
    points_per_side = int(time_per_side / control_dt) + 1  # 加1确保包含终点
    # 总点数（3条边）
    num_points = points_per_side * 3

    # 初始化轨迹数组
    trajectory_positions = np.zeros((num_points, 3))  # 位置 [x, y, z]
    trajectory_orientations = np.zeros((num_points, 4))  # 姿态 [w, x, y, z]
    trajectory_velocities = np.zeros((num_points, 3))  # 线速度 [vx, vy, vz]
    trajectory_angular_velocities = np.zeros((num_points, 3))  # 角速度 [wx, wy, wz]

    # 提取初始位置和姿态
    start_position = position_sequence[0]
    start_orientation = orientation_sequence[0]

    # 等边三角形的几何参数
    # 第一条边：沿X正方向
    # 第二条边：沿120度方向（相对于X轴正方向，逆时针）
    # 第三条边：沿240度方向（回到起点）
    cos_120 = np.cos(2 * np.pi / 3)  # cos(120°)
    sin_120 = np.sin(2 * np.pi / 3)  # sin(120°)
    cos_240 = np.cos(4 * np.pi / 3)  # cos(240°)
    sin_240 = np.sin(4 * np.pi / 3)  # sin(240°)

    # 定义三角形的三个阶段
    for i in range(num_points):
        # 确定当前所在的边
        side = i // points_per_side
        side_progress = (i % points_per_side) * control_dt * speed

        if side == 0:  # 第一条边：沿X正方向
            trajectory_positions[i, :] = [
                start_position[0] + side_progress,
                start_position[1],
                start_position[2]
            ]
            trajectory_velocities[i, :] = [speed, 0, 0]
        elif side == 1:  # 第二条边：沿120度方向
            trajectory_positions[i, :] = [
                start_position[0] + length + side_progress * cos_120,
                start_position[1] + side_progress * sin_120,
                start_position[2]
            ]
            trajectory_velocities[i, :] = [speed * cos_120, speed * sin_120, 0]
        else:  # 第三条边：沿240度方向（回到起点）
            # 第二顶点坐标
            x2 = start_position[0] + length
            y2 = start_position[1]
            trajectory_positions[i, :] = [
                x2 + length * cos_120 + side_progress * cos_240,
                y2 + length * sin_120 + side_progress * sin_240,
                start_position[2]
            ]
            trajectory_velocities[i, :] = [speed * cos_240, speed * sin_240, 0]

        # 姿态保持不变
        trajectory_orientations[i, :] = start_orientation
        # 角速度为零
        trajectory_angular_velocities[i, :] = [0, 0, 0]

    return trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities


# 可视化生成的轨迹
def plot_trajectory(trajectory_positions):
    """
    可视化生成的轨迹
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(trajectory_positions[:, 0], trajectory_positions[:, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    plt.title("Straight Line Trajectory")
    plt.show()




if __name__ == "__main__":
    traj_length = 0.35  # 轨迹长度：5 米
    speed = 0.01  # 速度：1 米/秒
    dt = 0.008  # 控制频率：125 Hz
    position_sequence = np.zeros((1, 3))
    print(position_sequence)
    orientation_sequence = np.array([[1, 0, 0, 0]])

    # trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = (
    #     generate_straight_trajectory(traj_length, dt, speed, position_sequence, orientation_sequence))
    
    trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = (
        generate_rectangular_trajectory(traj_length, dt, speed, position_sequence, orientation_sequence))
    
    trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = (
        generate_triangular_trajectory(traj_length, dt, speed, position_sequence, orientation_sequence))
    print(trajectory_positions)

    # c_p = np.concatenate((trajectory_positions[3, [0, 2]], trajectory_velocities[3, [0, 2]]))
    # c_p = np.concatenate((c_p, np.array([0, 0])))
    # print(c_p)
    # print( trajectory_positions[-1, 2])
    # print(len(trajectory_positions))
    # print(np.zeros((len(trajectory_positions), 2)))

    # fig = plt.figure()
    # ax = fig.add_subplot(111)

    # xx = np.array(trajectory_positions)
    # # ax.plot(xx[0,:], xx[1,:])
    # ax.plot(trajectory_positions[:, 0], trajectory_positions[:, 2])
    # ax.set_xlabel('X')
    # ax.set_ylabel('Z')
    # plt.title("Straight Line Trajectory")
    # plt.show()


    plot_trajectory(trajectory_positions)
