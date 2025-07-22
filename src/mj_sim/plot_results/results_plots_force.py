import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import pandas as pd
import numpy as np
# import trajectory_planner as traj
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

def cut_redundancy(arr):
    """
    找出一维 numpy 数组中最后一个不重复数字的索引。
    比如：[1,2,3,4,5,5,5] -> 返回索引 4
    """
    if len(arr) == 0:
        return -1  # 空数组返回 -1

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] != arr[-1]:
            return i + 1
    return -1  # 全部元素都相同时返回 -1

def calculate_rms_error(pos_vector_0, pos_vector_1, ref_pos_0, ref_pos_1):
    """
    Calculate the Root-Mean-Square (RMS) position error.
    
    Parameters:
    pos_vector_0 (numpy.ndarray): Robot's x position vector
    pos_vector_1 (numpy.ndarray): Robot's y position vector
    ref_pos_0 (numpy.ndarray): Reference x position vector
    ref_pos_1 (numpy.ndarray): Reference y position vector
    
    Returns:
    float: RMS position error
    """
    # 检查输入向量长度是否一致
    if not (len(pos_vector_0) == len(pos_vector_1) == len(ref_pos_0) == len(ref_pos_1)):
        raise ValueError("All input vectors must have the same length")
    
    # 计算 x 和 y 方向的位置误差平方
    error_x_squared = (pos_vector_0 - ref_pos_0) ** 2
    error_y_squared = (pos_vector_1 - ref_pos_1) ** 2
    
    # 计算总误差平方和
    total_error_squared = error_x_squared + error_y_squared
    # total_error_squared = error_y_squared.copy()
    # 计算均方误差
    mean_error_squared = np.mean(total_error_squared)
    
    # 计算 RMS 误差
    rms_error = np.sqrt(mean_error_squared)
    
    return rms_error


def plot_force(path_1, path_2):
    # Read the CSV file
    # df = pd.read_csv(path, sep='\t')
        # 声明参数并提供默认值

    # 从 CSV 文件加载数据
    data_array = np.genfromtxt(path_1, delimiter=',', skip_header=1)
    ref_array = np.genfromtxt(path_2, delimiter=',', skip_header=1)
    
    # 提取第 7 列 (pos_vector_0) 和第 8 列 (pos_vector_1)（0-based 索引为 6 和 7）
    ref_pos_0 = ref_array[:, 1]
    ref_pos_1 = ref_array[:, 2]
    item = cut_redundancy(ref_pos_1)
    print(item)
    force_vector_0 = data_array[:, 1][:item+1]
    force_vector_1 = data_array[:, 2][:item+1]
    pos_vector_0 = data_array[:, 7][:item+1]
    pos_vector_1 = data_array[:, 8][:item+1]
    ref_pos_0 = ref_pos_0[:item+1]
    ref_pos_1 = ref_pos_1[:item+1]
    print("mean_force_x", np.mean(np.abs(force_vector_0)))
    print("mean_force_y", np.mean(np.abs(force_vector_1)))
    print('max_f_x', max(np.abs(force_vector_0)))
    print('max_f_y', max(np.abs(force_vector_1)))
    rms = calculate_rms_error(pos_vector_0, pos_vector_1, ref_pos_0, ref_pos_1)
    print("pos RMS", rms)

    # Create figure with three subplots
    plt.figure(figsize=(12, 8))

    # Plot 1: pos_vector_0 vs index
    plt.subplot(3, 1, 1)
    plt.plot(force_vector_0, color='b', label = 'fx')
    plt.plot(force_vector_1, color='r', label = 'fx')
    plt.legend()
    plt.xlabel('Index')
    plt.ylabel('force_vector_0')
    plt.ylabel('force_vector_1')
    # plt.title('pos_vector_0 vs Index')
    plt.grid(True)


    # Plot 2: pos_vector_1 vs index
    plt.subplot(3, 1, 2)
    plt.xlabel('Index')
    plt.plot(ref_pos_0, color='b', label = 'ref_x')
    plt.plot(pos_vector_0, color='r', label = 'pos_x')
    plt.legend()
    # plt.title('pos_vector_1 vs Index')
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.xlabel('Index')
    plt.plot(ref_pos_1, color='b', label = 'ref_y')
    plt.plot(pos_vector_1, color='r', label = 'pos_y')
    plt.legend()
    # plt.title('pos_vector_1 vs Index')
    plt.grid(True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    path_1 = "/home/yanji/rosbag_record/mpc_gp_count/copy_a/para_a_60_3/rob_status.csv"
    path_2 = "/home/yanji/rosbag_record/mpc_gp_count/copy_a/para_a_60_3/ref_status.csv"
    # path_1 = "/home/yanji/rosbag_record/mpc_gp_state/para_a_3/rob_status.csv"
    # path_2 = "/home/yanji/rosbag_record/mpc_gp_state/para_a_3/ref_status.csv"
    # path = "/home/yanji/rosbag_record/mpc_track/triangular_01/rob_status.csv"
    plot_force(path_1, path_2)