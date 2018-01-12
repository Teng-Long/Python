#! python3.6
"""
    作者：杨杰
    功能：循环的进度条
    版本：0.1.0
    日期：2018-1-3
    许可证：GPL3+
    0.1.0 新增功能：循环的进度条（百分比显示 & 任务已完成提示）
"""

import time


if __name__ == '__main__':
    for i in range(1, 6):
        j = '#'
        for k in range(1, 61):
            j += '#'
            print('{:.2f}% |{}>'.format((k / 60) * 100, j), end='\r')
            time.sleep(0.017)
        print(' ' * 100, end='\r')
        print('任务 {}\t 已完成'.format(i))
    print('\n')
    input('Press <Enter>')
