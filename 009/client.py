#! python3.6
"""
新增功能：（1）网络命令用逗号代替空格
"""
import socket


def login():
    for i in range(3):
        print(' Login '.center(50, '*'))
        login_user = input('Login: ')
        socket_client.sendto('Login, {} '.format(login_user).encode('utf-8'), address_server)
        login_response = socket_client.recv(1024).split(b' ')[1]
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
        print('当前登录用户：{}'.format(login_user))


if __name__ == '__main__':
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address_server = ('127.0.0.1', 9999)

    main()
