#! python3.6
"""
    作者：杨杰
    功能：图书馆管理系统
    版本：0.2.0
    日期：2017-12-20
    许可证：GPL 3.0
    0.1.0 新增功能：服务器主界面
    TODO：0.2.0 新增功能：
"""


import sys


def print_main_menu():
    print('-' * 20, 'Book Borrowed System', '-' * 20)
    print('    1: Display all books')
    print('    2: Display your borrowed book\'s List')
    print('    3: Borrow a book')
    print('    4: Return a book')
    print('    0: quit')


def login():
    global login_user
    login_user = input('Login: ').lower()
    # 用户名必须是小写字母
    if login_user == 'ok':
        print('登录成功，正在进入系统')
        return True
    else:
        print('用户认证失败，系统退出！')
        return False


def main():
    if not login():
        sys.exit()
    while True:
        print_main_menu()
        choice = input('Please input your choice: ')
        if choice == '1':
            print('目前版本暂时不能提供服务！')
            pass
        elif choice == '2':
            print('目前版本暂时不能提供服务！')
            pass
        elif choice == '3':
            print('目前版本暂时不能提供服务！')
            pass
        elif choice == '4':
            print('目前版本暂时不能提供服务！')
            pass
        elif choice == '0':
            print('系统退出！')
            break


if __name__ == '__main__':
    main()
