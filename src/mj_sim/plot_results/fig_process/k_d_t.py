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
    #

    # 提取第 7 列 (pos_vector_0) 和第 8 列 (pos_vector_1)（0-based 索引为 6 和 7）
    k_0 = data_array[:len(trajectory_positions), 1]
    k_1 = data_array[:len(trajectory_positions), 2]
    d_0 = data_array[:len(trajectory_positions), 7]
    d_1 = data_array[:len(trajectory_positions), 8]

    font = {'family': 'serif', 'serif': 'Times New Roman', 'weight': 'normal', 'size': 20}
    plt.rc('font', **font)  # 其他部分（如刻度标签）继续使用 Times New Roman（由全局 plt.rc('font', **font) 控制）。
    mpl.rcParams.update({'font.size': 20, 'mathtext.fontset': 'stix'})
    mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    # 设置 SimSun 字体用于中文
    simsun = FontProperties(family='SimSun', size=20)


    # Create figure with three subplots
    plt.figure(figsize=(12, 6))

    # Plot 1: pos_vector_0 vs index
    plt.subplot(2, 1, 1)
    # plt.plot(k_0, color='b', label = "$k_x$")
    plt.plot(k_0, color='b', label="$k_x$")
    plt.plot(k_1, color='g', label = "$k_y$")
    plt.legend()
    plt.xlabel('步数', fontproperties=simsun, fontsize=20)
    plt.ylabel('${k}$')
    plt.grid(True)

    # Plot 2: pos_vector_1 vs index
    plt.subplot(2, 1, 2)
    plt.plot(d_0, color='b', label = "$d_x$")
    plt.plot(d_1, color='g', label = "$d_y$")
    plt.legend(loc='upper right')
    plt.xlabel('步数', fontproperties=simsun, fontsize=20)
    plt.ylabel('$d$')
    plt.grid(True)
    # plt.gca().yaxis.set_major_locator(MultipleLocator(0.01))

    # Adjust layout and display
    plt.tight_layout()
    # plt.savefig('figure/trian_k_d_y_t.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.savefig('figure/rect_distri_k_d_y_t.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()




if __name__ == "__main__":
    path = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_track\copy\rect_distri_7\cmd_status.csv"
    # path = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_track\copy\trian_5_3\cmd_status.csv"
    # path = "/home/yanji/rosbag_record/mpc_track/triangular_01/rob_status.csv"
    plot_trajectory(path)