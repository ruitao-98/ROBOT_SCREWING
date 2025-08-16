import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.font_manager import FontProperties
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter  # 引入 FormatStrFormatter
import os
import trajectory_planner as traj

def parse_subfolder(subfolder):
    """
    Parse subfolder name (e.g., para_a_15_1) to extract Parameter 1 and Parameter 2.
    Returns (param1, param2) as integers.
    """
    parts = subfolder.split('_')
    param1 = int(parts[2])  # e.g., 15 from para_a_15_1
    param2 = int(parts[3])  # e.g., 1 from para_a_15_1
    return param1, param2


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
    # print("pos_vector_0", pos_vector_0)
    # print("ref_vector_0", ref_pos_0)
    # print("pos_vector_1", pos_vector_1)
    # print("ref_vector_1", ref_pos_1)

    # 计算总误差平方和
    total_error_squared = error_x_squared + error_y_squared
    # total_error_squared = error_y_squared.copy()
    # 计算均方误差
    mean_error_squared = np.mean(total_error_squared)

    # 计算 RMS 误差
    rms_error = np.sqrt(mean_error_squared)

    return rms_error


def plot_statistics(csv_path0, csv_path1, csv_path2, csv_path3):
    """
    Create 3D surface plots for Mean_Force_X, Mean_Force_Y, and Pos_RMS.

    Parameters:
    csv_path (str): Path to the CSV file containing the data
    """
    rob_status0 = os.path.join(csv_path0, 'rob_status.csv')
    rob_status1 = os.path.join(csv_path1, 'rob_status.csv')
    rob_status2 = os.path.join(csv_path2, 'rob_status.csv')
    rob_status3 = os.path.join(csv_path3, 'rob_status.csv')

    ref_status0 = os.path.join(csv_path0, 'ref_status.csv')
    ref_status1 = os.path.join(csv_path1, 'ref_status.csv')
    ref_status2 = os.path.join(csv_path2, 'ref_status.csv')
    ref_status3 = os.path.join(csv_path3, 'ref_status.csv')

    # 从 CSV 文件加载数据
    status0 = np.genfromtxt(rob_status0, delimiter=',', skip_header=1)
    status1 = np.genfromtxt(rob_status1, delimiter=',', skip_header=1)
    status2 = np.genfromtxt(rob_status2, delimiter=',', skip_header=1)
    status3 = np.genfromtxt(rob_status3, delimiter=',', skip_header=1)

    refstatus0 = np.genfromtxt(ref_status0, delimiter=',', skip_header=1)
    refstatus1 = np.genfromtxt(ref_status1, delimiter=',', skip_header=1)
    refstatus2 = np.genfromtxt(ref_status2, delimiter=',', skip_header=1)
    refstatus3 = np.genfromtxt(ref_status3, delimiter=',', skip_header=1)

    refstatus0_x0 = refstatus0[:, 1]
    refstatus0_y0 = refstatus0[:, 2]
    item = cut_redundancy(refstatus0_y0)
    print('item=', item)
    refstatus0_x0 = refstatus0[:, 1][:item+1]
    refstatus0_y0 = refstatus0[:, 2][:item+1]

    # 提取第 7 列 (pos_vector_0) 和第 8 列 (pos_vector_1)（0-based 索引为 6 和 7）
    pos_vector_x0 = status0[:, 7][:item+1]
    pos_vector_y0 = status0[:, 8][:item+1]
    pos_vector_x1 = status1[:, 7][:item+1]
    pos_vector_y1 = status1[:, 8][:item+1]
    pos_vector_x2 = status2[:, 7][:item+1]
    pos_vector_y2 = status2[:, 8][:item+1]
    pos_vector_x3 = status3[:, 7][:item+1]
    pos_vector_y3 = status3[:, 8][:item+1]

    force_vector_x0 = status0[:, 1][:item+1]
    force_vector_y0 = status0[:, 2][:item+1]
    force_vector_x1 = status1[:, 1][:item+1]
    force_vector_y1 = status1[:, 2][:item+1]
    force_vector_x2 = status2[:, 1][:item+1]
    force_vector_y2 = status2[:, 2][:item+1]
    force_vector_x3 = status3[:, 1][:item+1]
    force_vector_y3 = status3[:, 2][:item+1]

    # Calculate metrics
    mean_force_x0 = np.mean(np.abs(force_vector_x0))
    mean_force_y0 = np.mean(np.abs(force_vector_y0))
    pos_rms_0 = calculate_rms_error(pos_vector_x0, pos_vector_y0, refstatus0_x0, refstatus0_y0)
    mean_force_x1 = np.mean(np.abs(force_vector_x1))
    mean_force_y1 = np.mean(np.abs(force_vector_y1))
    pos_rms_1 = calculate_rms_error(pos_vector_x1, pos_vector_y1, refstatus0_x0, refstatus0_y0)
    mean_force_x2 = np.mean(np.abs(force_vector_x2))
    mean_force_y2 = np.mean(np.abs(force_vector_y2))
    pos_rms_2 = calculate_rms_error(pos_vector_x2, pos_vector_y2, refstatus0_x0, refstatus0_y0)
    mean_force_x3 = np.mean(np.abs(force_vector_x3))
    mean_force_y3 = np.mean(np.abs(force_vector_y3))
    pos_rms_3 = calculate_rms_error(pos_vector_x3, pos_vector_y3, refstatus0_x0, refstatus0_y0)

    # font = {'family': 'serif', 'serif': 'Times New Roman', 'weight': 'normal', 'size': 20}
    # plt.rc('font', **font)  # 其他部分（如刻度标签）继续使用 Times New Roman（由全局 plt.rc('font', **font) 控制）。
    # mpl.rcParams.update({'font.size': 20, 'mathtext.fontset': 'stix'})
    # mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    # 设置 SimSun 字体用于中文
    # simsun = FontProperties(family='SimSun', size=20)
    # Create figure with three subplots

    # Bar Chart 1: Mean Forces Comparison
    fig2 = plt.figure(figsize=(8, 10))
    labels = ['MPC-GP', 'MPC', 'LAC', 'SAC']
    x = np.arange(len(labels))
    width = 0.35  # Width of the bars

    # Mean force data
    mean_forces_x = [mean_force_x0, mean_force_x1, mean_force_x2, mean_force_x3]
    mean_forces_y = [mean_force_y0, mean_force_y1, mean_force_y2, mean_force_y3]

    print("mean_force_x = ", mean_forces_x)
    print("mean_force_y = ", mean_forces_y)


    # Plot bars
    ax3 = fig2.add_subplot(211)
    ax3.bar(x - width / 2, mean_forces_x, width, label=r'Mean $F_x$', color='r')
    ax3.bar(x + width / 2, mean_forces_y, width, label=r'Mean $F_y$', color='b')
    ax3.set_ylabel(r'Mean Force [$\rm N$]')
    ax3.set_xticks(x)
    ax3.set_xticklabels(labels)
    ax3.legend()
    plt.grid(True, axis='y')
    # plt.savefig('figure/mean_forces_comparison.svg', dpi=300, format="svg", bbox_inches='tight')
    # plt.show()
    # plt.close()

    # Bar Chart 2: Positional RMS Error Comparison
    # fig3 = plt.figure(figsize=(8, 6))
    pos_rms = [pos_rms_0, pos_rms_1, pos_rms_2, pos_rms_3]
    print("pos_rms = ", pos_rms)
    ax4 = fig2.add_subplot(212)
    ax4.bar(labels, pos_rms, color='purple')
    ax4.set_ylabel(r'Positional RMS Error [$\rm m$]')
    # ax4.set_xticklabels(labels, fontproperties=simsun, fontsize=16)
    plt.grid(True, axis='y')
    plt.savefig('figure/pos_rms_comparison.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()
    plt.close()


# if __name__ == "__main__":
#     csv_path0 = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_gp_count\copy_a\para_a_60_3"
#     csv_path1 = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\compared_experiment\copy\para_a_1_5"  # Adjust path if needed
#     csv_path2 = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\compared_experiment\copy\para_a_2"
#     csv_path3 = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\compared_experiment\copy\para_a_3"


#     plot_statistics(csv_path0, csv_path1, csv_path2, csv_path3)