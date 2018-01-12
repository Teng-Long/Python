#! python3.6
"""
    作者：杨杰
    功能：模拟掷色子
    版本：0.2.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：（1）模拟抛掷一个色子，并输出其结果
                    （2）遍历列表时，同时返回索引号和值
    0.2.0 更新功能：模拟抛掷两个色子
"""
import random


def roll_dice():
    points = random.randint(1, 6)
    return points


def main():
    # input
    total_times = 10000
    result_list = [0] * 12
    point_list = list(range(2, 13))
    result_dict = dict(zip(point_list, result_list))

    # 掷色子
    for i in range(total_times):
        points_1 = roll_dice()
        points_2 = roll_dice()
        for j in range(2, 13):
            if (points_1 + points_2) == j:
                result_dict[j] += 1

    # output
    for i, times in result_dict.items():
        print('点数 {} 的次数为 {}，频率为 {}'.format(i, times, times / total_times))


if __name__ == '__main__':
    main()
