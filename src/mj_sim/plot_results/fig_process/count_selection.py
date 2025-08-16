import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.font_manager import FontProperties
import matplotlib as mpl

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
    param1_values = [15, 30, 60, 120]
    param2_values = [1, 3, 5, 7]

    # Create meshgrid for 3D plotting
    X, Y = np.meshgrid(param1_values, param2_values)
    Z_mean_force_x = np.zeros_like(X, dtype=float)
    Z_mean_force_y = np.zeros_like(X, dtype=float)
    Z_mean_force_resultant = np.zeros_like(X, dtype=float)
    Z_pos_rms = np.zeros_like(X, dtype=float)

    # Fill Z values
    for _, row in df.iterrows():
        param1, param2 = parse_subfolder(row['Subfolder'])
        i = param2_values.index(param2)  # Row index
        j = param1_values.index(param1)  # Column index
        Z_mean_force_x[i, j] = row['Mean_Force_X']
        Z_mean_force_y[i, j] = row['Mean_Force_Y']
        Z_mean_force_resultant[i, j] = row['Mean_Force_Resultant']
        Z_pos_rms[i, j] = row['Pos_RMS']*1000

    font = {'family': 'serif', 'serif': 'Times New Roman', 'weight': 'normal', 'size': 20}
    plt.rc('font', **font)  # 其他部分（如刻度标签）继续使用 Times New Roman（由全局 plt.rc('font', **font) 控制）。
    mpl.rcParams.update({'font.size': 20, 'mathtext.fontset': 'stix'})
    mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    # 设置 SimSun 字体用于中文
    simsun = FontProperties(family='SimSun', size=20)

    # Create figure with three subplots
    fig = plt.figure(figsize=(12, 6))

    # Plot 1: Mean_Force_X
    ax1 = fig.add_subplot(121, projection='3d')
    surf1 = ax1.plot_surface(X, Y, Z_mean_force_x, cmap=cm.viridis)
    ax1.set_xticks(param1_values)  # Set x-axis ticks to data values only
    ax1.set_yticks(param2_values)  # Set y-axis ticks to data values only
    # ax1.set_xlabel('参数1', fontproperties=simsun, fontsize=20)
    # ax1.set_ylabel('参数2', fontproperties=simsun, fontsize=20)
    # ax1.set_zlabel('$F_x$均值', fontproperties=simsun, fontsize=20)
    # fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
    ax1.view_init(elev=40, azim=-40)  # elev是垂直角度，azim是水平角度 b

    # Plot 2: Mean_Force_Y
    ax2 = fig.add_subplot(122, projection='3d')
    surf2 = ax2.plot_surface(X, Y, Z_mean_force_y, cmap=cm.viridis)
    ax2.set_xticks(param1_values)  # Set x-axis ticks to data values only
    ax2.set_yticks(param2_values)  # Set y-axis ticks to data values only
    ax2.zaxis.set_tick_params(labelleft=True, labelright=False)  # 将 z 轴刻度标签移到左边
    ax2.zaxis.set_tick_params(pad=10)  # 增加与图形的距离
    # ax2.set_xlabel('参数1', fontproperties=simsun, fontsize=20)
    # ax2.set_ylabel('参数2', fontproperties=simsun, fontsize=20)
    # ax1.set_zlabel('$F_y$均值', fontproperties=simsun, fontsize=20)
    # fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)
    # plt.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.1)  # 调整画布的边距
    ax2.view_init(elev=40, azim=-40)  # elev是垂直角度，azim是水平角度 b
    plt.tight_layout(pad=2.0)  # 增加布局间距
    plt.savefig('figure/count_force_b.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()

    fig = plt.figure(figsize=(6, 6))
    # Plot 4: Pos_RMS
    ax4 = fig.add_subplot(111, projection='3d')
    surf4 = ax4.plot_surface(X, Y, Z_pos_rms, cmap=cm.viridis)
    ax4.set_xticks(param1_values)  # Set x-axis ticks to data values only
    ax4.set_yticks(param2_values)  # Set y-axis ticks to data values only
    ax4.zaxis.set_tick_params(pad=5)  # 增加与图形的距离
    # ax4.set_xlabel('参数1', fontproperties=simsun, fontsize=20)
    # ax4.set_ylabel('参数2', fontproperties=simsun, fontsize=20)
    # ax4.set_zlabel('位置误差', fontproperties=simsun, fontsize=20)
    # ax4.view_init(elev=30, azim=120)  # elev是垂直角度，azim是水平角度 a
    ax4.view_init(elev=35, azim=160)  # elev是垂直角度，azim是水平角度 b
    ax4.zaxis.set_tick_params(labelleft=True, labelright=False)  # 将 z 轴刻度标签移到左边
    # plt.tight_layout(pad=2.0)  # 调整布局的填充
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # 调整画布的边距
    plt.savefig('figure/count_pos_err_b.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    csv_path = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_gp_count\copy_b\results.csv"  # Adjust path if needed
    plot_3d_metrics(csv_path)