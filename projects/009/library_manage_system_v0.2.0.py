#! python3.6
"""
    作者：杨杰
    功能：图书馆管理系统
    版本：0.2.0
    日期：2017-12-20
    许可证：GPL 3.0
    对应服务器版本：0.6.0
    0.1.0 新增功能：服务器主界面
    0.2.0 新增功能：用户登录，利用参数 Login
"""
import socket


def print_main_menu(login_user):
    print(' 图书馆管理系统 '.center(50, '*'))
    print('当前登录用户：{}'.format(login_user))
    print('    1: Display all books')
    print('    2: Display your borrowed book\'s List')
    print('    3: Borrow a book')
    print('    4: Return a book')
    print('    0: Logout')


def login():
    for i in range(3):
        print(' Login '.center(50, '*'))
        login_user = input('Login: ')
        client_socket.sendto('Login {}'.format(login_user).encode('utf-8'), address_server)
        login_response = client_socket.recv(1024).split(b' ')[1]
        if login_response == b'OK':
            print('登录成功，正在进入系统')
            return login_user
        else:
            if i == 2:
                print('用户认证失败3次，系统退出！')
                return False
            else:
                print('用户认证失败，请重新登录！')
                print('当前失败次数：', i + 1)


def main():
    login_user = login()
    if login_user:
        while True:
            print_main_menu(login_user)
            choice = input('Please input your choice: ')
            if choice == '1':
                print('目前版本暂时不能提供服务！')
            elif choice == '2':
                print('目前版本暂时不能提供服务！')
            elif choice == '3':
                print('目前版本暂时不能提供服务！')
            elif choice == '4':
                print('目前版本暂时不能提供服务！')
            elif choice == '0':
                print('系统退出！')
                break
            else:
                print('错误的输入，程序返回！')


if __name__ == '__main__':
    # 初始化网络套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address_server = ('127.0.0.1', 9999)

    main()
