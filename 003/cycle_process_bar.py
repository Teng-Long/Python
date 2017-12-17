#! python3.6


import time


def cycle_process_bar(width, rate, hash_number):
    width += hash_number
    while True:
        for i in range(width):
            str_obj = '[' + (' ' * (i % width) + '#' * hash_number + ' ' * (width - i % width))[hash_number:width] + ']'
            print(str_obj, end="\r")
            time.sleep(rate)


if __name__ == '__main__':
    cycle_process_bar(int(input("请输入进度条的总长度（单位：字符）：")), float(input("请输入进度的刷新速率（单位秒/次)")), int(input("请输入进度（单位：字符）")))
    print("\n")
    input("Press <Enter>")
