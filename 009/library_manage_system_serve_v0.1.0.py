#! python3.6
"""
    作者：杨杰
    功能：图书馆管理系统（服务端）
    版本：0.1.0
    日期：2017-12-20
    许可证：GPL 3.0
    0.1.0 功能：在服务器创建线程，运行 10s，并输出信息
"""
import threading
import time


def manage_thread():
    print('线程1已运行')
    i = 0
    while True:
        time.sleep(1)
        i += 1
        print('线程1正在运行，%ss' % str(i))
        if i == 10:
            break
    pass


def communication_thread():
    print('线程2已运行')
    j = 0
    while True:
        time.sleep(1)
        j += 1
        print('线程2正在运行，%ss' % str(j))
        if j == 5:
            break
    pass


def main():
    thread_1 = threading.Thread(target=manage_thread, name='Manage Thread')
    thread_2 = threading.Thread(target=communication_thread, name='Communication Thread')
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    print('\n')
    input('Press <Enter>')


if __name__ == '__main__':
    main()
