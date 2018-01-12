#! python3.6
"""
    作者：杨杰
    功能：模拟掷色子
    版本：0.3.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：（1）模拟抛掷一个色子，并输出其结果
                    （2）遍历列表时，同时返回索引号和值
    0.2.0 更新功能：模拟抛掷两个色子
    0.3.0 新增功能：可视化抛掷两个色子的结果
"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    points = random.randint(1, 6)
    return points


def main():
    # input
    total_times = 1000
    result_list = [0] * 12
    point_list = list(range(2, 13))
    result_dict = dict(zip(point_list, result_list))
    point_1_list = []
    point_2_list = []

    # 掷色子
    for i in range(total_times):
        points_1 = roll_dice()
        points_2 = roll_dice()
        point_1_list.append(points_1)
        point_2_list.append(points_2)
        for j in range(2, 13):
            if (points_1 + points_2) == j:
                result_dict[j] += 1

    # 数据可视化 散点图 坐标列表
    x = list(range(1, total_times + 1))
    plt.scatter(x, point_1_list, c='red', alpha=0.5)
    plt.scatter(x, point_2_list, c='green', alpha=0.5)

    # output
    for i, times in result_dict.items():
        print('点数 {} 的次数为 {}，频率为 {}'.format(i, times, times / total_times))
    plt.show()


if __name__ == '__main__':
    main()
