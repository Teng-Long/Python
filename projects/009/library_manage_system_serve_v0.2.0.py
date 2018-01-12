#! python3.6
"""
    作者：杨杰
    功能：图书馆管理系统（服务端）
    版本：0.2.0
    日期：2017-12-20
    许可证：GPL 3.0
    0.1.0 功能：在服务器创建线程，运行 10s，并输出信息
    0.2.0 新增功能：在管理线程中，运行本地的图书馆管理系统
"""
import threading


def print_main_menu():
    print(' 图书馆管理系统 '.center(50, '*'))
    print('    1: Display all books')
    print('    2: User management')
    print('    3: Book management')
    print('    0: Quit')


def manage_thread():
    print('线程1已运行')
    while True:
        print_main_menu()
        choice = input('Please input: ')
        if choice == '1':
            print('当前版本暂不支持此功能，程序返回')
            pass
        elif choice == '2':
            print('当前版本暂不支持此功能，程序返回')
            pass
        elif choice == '3':
            print('当前版本暂不支持此功能，程序返回')
            pass
        elif choice == '0':
            break
    print('线程1已停止运行')


def communication_thread():
    pass


def main():
    thread_1 = threading.Thread(target=manage_thread, name='Manage Thread')
    thread_2 = threading.Thread(target=communication_thread, name='Communication Thread')
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()


if __name__ == '__main__':
    main()
