#! python3.6
"""
    作者：杨杰
    功能：模拟掷色子
    版本：0.5.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：（1）模拟抛掷一个色子，并输出其结果
                    （2）遍历列表时，同时返回索引号和值
    0.2.0 更新功能：模拟抛掷两个色子
    0.3.0 新增功能：可视化抛掷两个色子的结果
    0.4.0 更新功能：对结果进行简单的数据统计和分析
    0.5.0 更新功能：使用科学计算库简化程序，完善数据可视化结果
"""
import matplotlib.pyplot as plt
import numpy as np


def main():
    # input
    total_times = 10000

    # 生成随机数组
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=list(range(2, 14)))
    print(hist)
    print(bins)

    # 数据可视化

    plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置字体为黑体
    plt.rcParams['axes.unicode_minus'] = False      # 设置负号为 False
    plt.hist(result_arr, bins=list(range(2, 14)), normed=1, edgecolor='black', linewidth=1, rwidth=0.6)
    # 设置 x 轴坐标点显示
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_position = np.arange(2, 13) + 0.5
    plt.xticks(tick_position, tick_labels)

    plt.title('色子点数频率直方图')
    plt.xlabel('点数')
    plt.ylabel('频率')

    # output
    plt.show()


if __name__ == '__main__':
    main()
