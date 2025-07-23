import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.font_manager import FontProperties

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
    labels = ["A", "B", "C", "D"]
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
        Z_mean_force_resultant[i] = row['Mean_Force_Resultant']
        Z_pos_rms[i] = row['Pos_RMS']
        Time[i] = row["Time"]
        i = i + 1
    
    # Create figure with three subplots
    fig = plt.figure(figsize=(24, 6))
    x_indices = np.arange(len(labels))
    # Plot 1: Mean_Force_X
    ax1 = fig.add_subplot(141)
    ax1.plot(x_indices, Z_mean_force_x)
    ax1.set_xticks(x_indices)
    ax1.set_xticklabels(labels)
    # ax1.set_xticks(param_values)  # Set x-axis ticks to data values only
    ax1.set_ylabel('Mean_Force_X', fontproperties=font)
    ax1.set_title('Mean_Force_X 分布', fontproperties=font)


    ax2 = fig.add_subplot(142)
    ax2.plot(x_indices, Z_mean_force_y)
    ax2.set_xticks(x_indices)
    ax2.set_xticklabels(labels)
    ax2.set_ylabel('Mean_Force_Y', fontproperties=font)
    ax2.set_title('Mean_Force_Y 分布', fontproperties=font)

    ax3 = fig.add_subplot(143)
    ax3.plot(x_indices, Z_pos_rms)
    ax3.set_xticks(x_indices)
    ax3.set_xticklabels(labels)
    ax3.set_ylabel('Pos_RMS', fontproperties=font)
    ax3.set_title('Pos_RMS 分布', fontproperties=font)

    ax4 = fig.add_subplot(144)
    ax4.plot(x_indices, Time)
    ax4.set_xticks(x_indices)
    ax4.set_xticklabels(labels)
    ax4.set_ylabel('Time', fontproperties=font)
    ax4.set_title('Time 分布', fontproperties=font)

    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    csv_path = "/home/yanji/rosbag_record/mpc_gp_state/results_b.csv"  # Adjust path if needed
    plot_3d_metrics(csv_path)