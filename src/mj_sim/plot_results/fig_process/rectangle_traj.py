import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import pandas as pd
import numpy as np
import trajectory_planner as traj
from matplotlib.ticker import MultipleLocator
import matplotlib as mpl

# matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
# matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
font = FontProperties(fname=None, family='AR PL UMing CN', size=12)  # 如果系统中没有 SimHei，可替换为其他字体


def plot_time(Time, mean):
    plt.figure(figsize=(10, 6))
    plt.plot(Time, label='MPC Execution Time (ms)')
    plt.axhline(y=mean, color='r', linestyle='--', label=f'Mean: {mean:.2f} ms')
    plt.xlabel('迭代次数', fontproperties=font)
    plt.ylabel('时间 (ms)', fontproperties=font)
    # plt.title('MPC Execution Time Over Iterations')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_trajectory(path):
    # Read the CSV file
    # df = pd.read_csv(path, sep='\t')
    # 声明参数并提供默认值

    # 从 CSV 文件加载数据
    data_array = np.genfromtxt(path, delimiter=',', skip_header=1)

    # 调试：检查数据形状
    print("Data shape:", data_array.shape)
    if data_array.ndim == 1:
        print("Error: Data is 1-dimensional. Checking first few rows of file:")
        with open(path, 'r') as f:
            for i, line in enumerate(f):
                if i < 5:  # 打印前 5 行
                    print(f"Line {i}: {line.strip()}")
        raise ValueError("Loaded data is 1-dimensional. Please check file format or delimiter.")

    # 提取第 7 列 (pos_vector_0) 和第 8 列 (pos_vector_1)（0-based 索引为 6 和 7）
    pos_vector_0 = data_array[:, 7]
    pos_vector_1 = data_array[:, 8]
    pos_vector_2 = data_array[:, 9]
    print(data_array[0, :])

    start_pos_np = np.array([pos_vector_0[0], pos_vector_1[0], pos_vector_2[0]])
    start_rotm_np = np.array(data_array[0, 10:19]).reshape(3, 3)

    # 获得参数，重新生成轨迹，用于mpc计算
    t0 = 0.0
    traj_length = 0.07
    speed = 0.01
    dt = 0.008
    position_sequence = np.array([[0.0, 0.0, 0.0]])
    orientation_sequence = np.array([[1.0, 0.0, 0.0, 0.0]])

    # trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = traj.generate_straight_trajectory(traj_length, dt,
    #                                                                                                                                         speed, position_sequence,
    #                                                                                                                                         orientation_sequence) #生成x方向的直线轨迹
    trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = traj.generate_rectangular_trajectory(
        traj_length, dt,
        speed, position_sequence,
        orientation_sequence)  # 生成x方向的直线轨迹
    # trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = (traj.generate_triangular_trajectory(traj_length, dt,
    #                                                                                                                                            speed, position_sequence,
    #                                                                                                                                            orientation_sequence)) #生成x方向的直线轨迹
    traj_1 = np.hstack((trajectory_positions[:, [0]], trajectory_velocities[:, [0]]))
    traj_1 = np.hstack((traj_1, np.zeros((len(trajectory_positions), 1))))
    traj_2 = np.hstack((trajectory_positions[:, [1]], trajectory_velocities[:, [1]]))
    traj_2 = np.hstack((traj_2, np.zeros((len(trajectory_positions), 1))))
    traj_3 = np.hstack((trajectory_positions[:, [2]], trajectory_velocities[:, [2]]))
    traj_3 = np.hstack((traj_3, np.zeros((len(trajectory_positions), 1))))

    traj_all = np.hstack((traj_1, traj_2, traj_3))  # x * 9，只包括x y z 不包括旋转

    traj_all_base = traj_all.copy()

    for local_i in range(len(traj_all)):
        incre_pos = np.array([traj_all[local_i, 0], traj_all[local_i, 3], traj_all[local_i, 6]])
        action_pos = start_pos_np + start_rotm_np @ incre_pos
        incre_vel = np.array([traj_all[local_i, 1], traj_all[local_i, 4], traj_all[local_i, 7]])
        action_vel = start_rotm_np @ incre_vel

        assert action_pos.shape[0] == 3, "action_pos must have 3 elements"
        traj_all_base[local_i, [0, 3, 6]] = action_pos
        traj_all_base[local_i, [1, 4, 7]] = action_vel

    trajectory_positions[:, 0] = trajectory_positions[:, 0] + pos_vector_0[0]
    trajectory_positions[:, 1] = trajectory_positions[:, 1] + pos_vector_1[0]

    font = {'family': 'serif', 'serif': 'Times New Roman', 'weight': 'normal', 'size': 20}
    plt.rc('font', **font)  # 其他部分（如刻度标签）继续使用 Times New Roman（由全局 plt.rc('font', **font) 控制）。
    mpl.rcParams.update({'font.size': 20, 'mathtext.fontset': 'stix'})
    mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    # 设置 SimSun 字体用于中文
    simsun = FontProperties(family='SimSun', size=20)

    # Create figure with three subplots
    plt.figure(figsize=(7, 7))

    # Plot 1: pos_vector_0 vs index
    plt.subplot(2, 1, 1)
    plt.plot(pos_vector_0[: len(trajectory_positions)], color='mediumblue', linewidth=2)
    plt.plot(traj_all_base[:, 0], color='black', linestyle='--', linewidth=2)
    plt.xlabel('步数', fontproperties=simsun, fontsize=20)
    plt.ylabel('$x$[m]')
    plt.grid(True)

    # Plot 2: pos_vector_1 vs index
    plt.subplot(2, 1, 2)
    plt.plot(pos_vector_1[: len(trajectory_positions)], color='seagreen', linewidth=2)
    plt.plot(traj_all_base[:, 3], color='black', linestyle='--', linewidth=2)
    plt.axhline(y=0.42, color='red', linestyle='--', linewidth=2)
    plt.xlabel('步数', fontproperties=simsun, fontsize=20)
    plt.ylabel('$y$[m]')
    plt.grid(True)
    # plt.gca().yaxis.set_major_locator(MultipleLocator(0.01))

    # Adjust layout and display
    plt.tight_layout()
    # plt.savefig('figure/trian_xy_t.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.savefig('figure/rect_distri_xy_t.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()

    plt.figure(figsize=(7, 7))
    # Plot 3: Scatter plot of pos_vector_0 vs pos_vector_1
    plt.subplot(1, 1, 1)
    plt.plot(pos_vector_0[: len(trajectory_positions)], pos_vector_1[: len(trajectory_positions)], color='b', linewidth = 3)

    plt.plot(traj_all_base[:, 0], traj_all_base[:, 3], color='black', linewidth = 2, linestyle='--')
    # 添加 y=0.42 的红色虚线横线
    plt.axhline(y=0.42, color='red', linestyle='--', linewidth=2)

    plt.xlabel('$x$[m]')
    plt.ylabel('$y$[m]')
    plt.grid(True)

    # Adjust layout and display
    plt.tight_layout()
    # plt.savefig('figure/trian_xy.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.savefig('figure/rect_distri_xy.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    path = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_track\copy\rect_distri_7\rob_status.csv"
    # path = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_track\copy\trian_5_3\rob_status.csv"
    # path = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_track\copy\rect_6_5\rob_status.csv"
    # path = "/home/yanji/rosbag_record/mpc_track/triangular_01/rob_status.csv"
    plot_trajectory(path)