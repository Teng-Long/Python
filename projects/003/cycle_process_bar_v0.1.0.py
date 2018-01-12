#! python3.6
"""
    作者：杨杰
    功能：循环的进度条
    版本：0.1.0
    日期：2018-1-3
    许可证：GPL3+
    0.1.0 新增功能：循环的进度条
"""

import time


def cycle_process_bar(width, rate, hash_number):
    width += hash_number
    while True:
        for i in range(width):
            str_obj = '[' + (' ' * (i % width) + '#' * hash_number + ' ' * (width - i % width))[hash_number:width] + ']'
            print(str_obj, end="\r")
            time.sleep(rate)


if __name__ == '__main__':
    # 进度条的总长度（单位：字符）
    # 进度的刷新速率（单位秒/次)
    # 进度的长度（单位：字符）
    width = 100
    rate = 0.017
    hash_number = 30
    cycle_process_bar(width, rate, hash_number)
    print("\n")
    input("Press <Enter>")
