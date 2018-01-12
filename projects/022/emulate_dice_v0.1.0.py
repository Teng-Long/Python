#! python3.6
"""
    作者：杨杰
    功能：模拟掷色子
    版本：0.1.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：（1）模拟抛掷一个色子，并输出其结果
                    （2）遍历列表时，同时返回索引号和值
"""
import random


def roll_dice():
    points = random.randint(1, 6)
    return points


def main():
    # input
    total_times = 10000
    result_list = [0] * 6

    # 掷色子
    for i in range(total_times):
        points = roll_dice()
        for j in range(1, 7):
            if points == j:
                result_list[j - 1] += 1

    # output
    for i, times in enumerate(result_list):
        print('点数 {} 的次数为 {}，频率为 {}'.format(i + 1, times, times / total_times))


if __name__ == '__main__':
    main()
