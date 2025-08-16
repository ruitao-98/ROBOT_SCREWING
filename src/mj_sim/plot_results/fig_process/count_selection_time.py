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
    Z_time = np.zeros_like(X, dtype=float)

    # Fill Z values
    for _, row in df.iterrows():
        param1, param2 = parse_subfolder(row['Subfolder'])
        i = param2_values.index(param2)  # Row index
        j = param1_values.index(param1)  # Column index
        Z_time[i, j] = row['time']

    font = {'family': 'serif', 'serif': 'Times New Roman', 'weight': 'normal', 'size': 20}
    plt.rc('font', **font)  # 其他部分（如刻度标签）继续使用 Times New Roman（由全局 plt.rc('font', **font) 控制）。
    mpl.rcParams.update({'font.size': 20, 'mathtext.fontset': 'stix'})
    mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    # 设置 SimSun 字体用于中文
    simsun = FontProperties(family='SimSun', size=20)

    # Create figure with three subplots
    fig = plt.figure(figsize=(6, 6))

    # Plot 1: Mean_Force_X
    ax1 = fig.add_subplot(111, projection='3d')
    surf1 = ax1.plot_surface(X, Y, Z_time, cmap=cm.viridis)
    ax1.set_xticks(param1_values)  # Set x-axis ticks to data values only
    ax1.set_yticks(param2_values)  # Set y-axis ticks to data values only
    # ax1.set_xlabel('参数1', fontproperties=font)
    # ax1.set_ylabel('参数2', fontproperties=font)
    # ax1.set_zlabel('Time', fontproperties=font)
    # ax1.set_title('Time 分布', fontproperties=font)
    # fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
    ax1.view_init(elev=30, azim=120)  # elev是垂直角度，azim是水平角度
    # Adjust layout and display
    plt.tight_layout()
    plt.savefig('figure/count_time_b.svg', dpi=300, format="svg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    csv_path = r"E:\desktop\paper writing\Chapter_4\robot_screwing\rosbag_record\mpc_gp_count\copy_b\time.csv"  # Adjust path if needed
    plot_3d_metrics(csv_path)