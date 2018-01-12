#! python3.6
"""
    作者：杨杰
    功能：模拟掷色子
    版本：0.4.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：（1）模拟抛掷一个色子，并输出其结果
                    （2）遍历列表时，同时返回索引号和值
    0.2.0 更新功能：模拟抛掷两个色子
    0.3.0 新增功能：可视化抛掷两个色子的结果
    0.4.0 更新功能：对结果进行简单的数据统计和分析
"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    points = random.randint(1, 6)
    return points


def main():
    # input
    total_times = 10000
    point_list = []

    # 掷色子
    for i in range(total_times):
        points_1 = roll_dice()
        points_2 = roll_dice()
        point_list.append(points_1 + points_2)

    # 数据可视化
    plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置字体为黑体
    plt.rcParams['axes.unicode_minus'] = False      # 设置负号为 False
    plt.hist(point_list, bins=list(range(2, 14)), normed=1, edgecolor='black', linewidth=1)
    plt.title('色子点数频率直方图')
    plt.xlabel('点数')
    plt.ylabel('频率')

    # output
    plt.show()


if __name__ == '__main__':
    main()
