import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import pandas as pd
import numpy as np
import trajectory_planner as traj
from matplotlib.ticker import MultipleLocator
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
    print(data_array[0,:])

    start_pos_np = np.array([pos_vector_0[0], pos_vector_1[0], pos_vector_2[0]])
    start_rotm_np = np.array(data_array[0, 10:19]).reshape(3, 3)


    # 获得参数，重新生成轨迹，用于mpc计算
    t0 =                   0.0
    traj_length =          0.08
    speed =                0.01
    dt =                   0.008
    position_sequence =    np.array([[0.0, 0.0, 0.0]])
    orientation_sequence = np.array([[1.0, 0.0, 0.0, 0.0]])

    # trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = traj.generate_straight_trajectory(traj_length, dt, 
    #                                                                                                                                         speed, position_sequence, 
    #                                                                                                                                         orientation_sequence) #生成x方向的直线轨迹
    trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = traj.generate_rectangular_trajectory(traj_length, dt, 
                                                                                                                                            speed, position_sequence, 
                                                                                                                                            orientation_sequence) #生成x方向的直线轨迹
    # trajectory_positions, trajectory_orientations, trajectory_velocities, trajectory_angular_velocities = (traj.generate_triangular_trajectory(traj_length, dt, 
    #                                                                                                                                            speed, position_sequence, 
    #                                                                                                                                            orientation_sequence)) #生成x方向的直线轨迹
    traj_1 = np.hstack((trajectory_positions[:, [0]], trajectory_velocities[:, [0]]))
    traj_1 = np.hstack((traj_1, np.zeros((len(trajectory_positions), 1))))
    traj_2 = np.hstack((trajectory_positions[:, [1]], trajectory_velocities[:, [1]]))
    traj_2 = np.hstack((traj_2, np.zeros((len(trajectory_positions), 1))))
    traj_3 = np.hstack((trajectory_positions[:, [2]], trajectory_velocities[:, [2]]))
    traj_3 = np.hstack((traj_3, np.zeros((len(trajectory_positions), 1))))

    traj_all =  np.hstack((traj_1, traj_2, traj_3)) # x * 9，只包括x y z 不包括旋转

    traj_all_base = traj_all.copy()

    for local_i in range(len(traj_all)):
        incre_pos = np.array([traj_all[local_i, 0], traj_all[local_i, 3], traj_all[local_i, 6]])
        action_pos = start_pos_np + start_rotm_np @ incre_pos
        incre_vel = np.array([traj_all[local_i, 1], traj_all[local_i, 4], traj_all[local_i, 7]])
        action_vel = start_rotm_np @ incre_vel

        assert action_pos.shape[0] == 3, "action_pos must have 3 elements"
        traj_all_base[local_i, [0, 3, 6]] = action_pos
        traj_all_base[local_i, [1, 4, 7]] = action_vel



    trajectory_positions[:,0] = trajectory_positions[:,0] + pos_vector_0[0]
    trajectory_positions[:,1] = trajectory_positions[:,1] + pos_vector_1[0]
    # Create figure with three subplots
    plt.figure(figsize=(15, 5))

    # Plot 1: pos_vector_0 vs index
    plt.subplot(1, 3, 1)
    plt.plot(pos_vector_0, color='b')
    plt.plot(traj_all_base[:, 0], color='black')
    plt.xlabel('Index')
    plt.ylabel('pos_vector_0')
    plt.title('pos_vector_0 vs Index')
    plt.grid(True)

    # Plot 2: pos_vector_1 vs index
    plt.subplot(1, 3, 2)
    plt.plot(pos_vector_1 - pos_vector_1[0], color='r')
    plt.plot(traj_all_base[:, 3] - traj_all_base[0, 3], color='black')
    plt.xlabel('Index')
    plt.ylabel('pos_vector_1')
    plt.title('pos_vector_1 vs Index')
    plt.grid(True)
    plt.gca().yaxis.set_major_locator(MultipleLocator(0.01))
    
    # Plot 3: Scatter plot of pos_vector_0 vs pos_vector_1
    plt.subplot(1, 3, 3)
    plt.plot(pos_vector_0, pos_vector_1, color='g')

    plt.plot(traj_all_base[:, 0], traj_all_base[:, 3], color='black')
    plt.xlabel('pos_vector_0')
    plt.ylabel('pos_vector_1')
    plt.title('pos_vector_0 vs pos_vector_1')
    plt.grid(True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    path = "/home/yanji/rosbag_record/mpc_track/rectangular_05/rob_status.csv"
    # path = "/home/yanji/rosbag_record/mpc_track/triangular_01/rob_status.csv"
    plot_trajectory(path)