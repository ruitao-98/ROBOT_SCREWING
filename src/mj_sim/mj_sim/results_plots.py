import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
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