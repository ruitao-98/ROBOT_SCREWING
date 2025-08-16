import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.font_manager import FontProperties
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter  # 引入 FormatStrFormatter
# Set font for Chinese characters
font = FontProperties(fname=None, family='AR PL UMing CN', size=12)


def parse_subfolder(subfolder):
    """
    Parse subfolder name (e.g., para_a_15_1) to extract Parameter 1 and Parameter 2.
    Returns (param1, param2) as integers.
    """
    parts = subfolder.split('_')
    param1 = int(parts[2])  # e.g., 15 from para_a_15_1
    param2 = int(parts[3])  # e.g., 1 from para_a_15_1
    return param1, param2


def plot_3d_metrics(csv_path):
    """
    Create 3D surface plots for Mean_Force_X, Mean_Force_Y, and Pos_RMS.

    Parameters:
    csv_path (str): Path to the CSV file containing the data
    """
    # Read the CSV file
    df = pd.read_csv(csv_path)
    print(df)

    # Define parameter values
    labels = ["特征 $1$", "特征 $2$", "特征 $3$", "特征 $4$"]
    param_values = labels

    # Create meshgrid for 3D plotting
    Z_mean_force_x = np.ones(len(param_values))
    Z_mean_force_y = np.ones(len(param_values))
    Z_mean_force_resultant = np.ones(len(param_values))
    Z_pos_rms = np.ones(len(param_values))
    Time = np.ones(len(param_values))
    i = 0
    # Fill Z values
    for _, row in df.iterrows():
        Z_mean_force_x[i] = row['Mean_Force_X']
        Z_mean_force_y[i] = row['Mean_Force_Y']
        Z_mean_force_resultant[i] = row['Mean_Force_Resultant'] * 1000
        Z_pos_rms[i] = row['Pos_RMS'] * 1000
        Time[i] = row["Time"]
        i = i + 1
    font = {'family': 'serif', 'serif': 'Times New Roman', 'weight': 'normal', 'size': 20}
    plt.rc('font', **font)  # 其他部分（如刻度标签）继续使用 Times New Roman（由全局 plt.rc('font', **font) 控制）。
    mpl.rcParams.update({'font.size': 20, 'mathtext.fontset': 'stix'})
    mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    # 设置 SimSun 字体用于中文
    simsun = FontProperties(family='SimSun', size=20)
    # Create figure with three subplots
    fig = plt.figure(figsize=(15, 4))
    x_indices = np.arange(len(labels))
    # Plot 1: Mean_Force_X
    ax1 = fig.add_subplot(121)
    ax1.plot(x_indices, Z_mean_force_x, linewidth = 2, color = 'b')
    ax1.set_xticks(x_indices)
    ax1.set_xticklabels(labels, fontproperties=simsun, fontsize=20)
    # ax1.set_xticks(param_values)  # Set x-axis ticks to data values only
    ax1.set_ylabel(r'$F_x$ 均值 [$\rm N$]', fontproperties=simsun, fontsize=20)
    plt.grid(True)

    ax2 = fig.add_subplot(122)
    ax2.plot(x_indices, Z_mean_force_y, linewidth = 2, color = 'b')
    ax2.set_xticks(x_indices)
    ax2.set_xticklabels(labels, fontproperties=simsun, fontsize=20)
    ax2.set_ylabel(r'$F_y$ 均值 $[\rm N]$', fontproperties=simsun, fontsize=20)
    # Adjust layout and display
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('figure/feature_force_a.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()

    fig = plt.figure(figsize=(15, 4))
    ax3 = fig.add_subplot(121)
    ax3.plot(x_indices, Z_pos_rms, linewidth = 2, color = 'b')
    ax3.set_xticks(x_indices)
    ax3.set_xticklabels(labels, fontproperties=simsun, fontsize=20)
    ax3.set_ylabel(r'位置误差 $[\rm mm]$', fontproperties=simsun, fontsize=20)
    ax3.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))  # 限制 y 轴刻度为 3 位小数
    plt.grid(True)

    ax4 = fig.add_subplot(122)
    ax4.plot(x_indices, Time, linewidth = 2, color = 'b')
    ax4.set_xticks(x_indices)
    ax4.set_xticklabels(labels, fontproperties=simsun, fontsize=20)
    ax4.set_ylabel(r'时间$[\rm ms]$', fontproperties=simsun, fontsize=20)

    # Adjust layout and display
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('figure/feature_pos_a.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    csv_path = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_gp_state\results_a.csv"  # Adjust path if needed
    plot_3d_metrics(csv_path)