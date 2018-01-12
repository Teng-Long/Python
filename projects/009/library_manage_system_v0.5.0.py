#! python3.6
"""
    作者：杨杰
    功能：图书馆管理系统
    版本：0.5.0
    日期：2017-12-20
    许可证：GPL 3.0
    对应服务器版本：0.8.0
    0.1.0 新增功能：服务器主界面
    0.2.0 新增功能：用户登录，利用参数 Login
    0.3.0 新增功能：输出所有书籍，利用参数 Books_All
    0.4.0 新增功能：输出当前用户借出的书籍，利用参数 Books_Borrowed
    TODO: 0.5.0 新增功能：借书功能，利用参数 Borrow_Book
"""
import json
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
        socket_client.sendto('Login {}'.format(login_user).encode('utf-8'), address_server)
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


def display_all_books():
    print(' Display All Books '.center(50, '*'))
    print('|', 'BookID'.center(15), 'BookName'.center(15), 'Author'.center(15), 'Press'.center(15), 'Number'.center(15),
          '|')
    socket_client.sendto(b'Books_All', address_server)
    books = json.loads(socket_client.recv(1024).decode('utf-8'))
    for book in books:
        print('|', book['book_id'].center(15), book['book_name'].center(15), book['author'].center(15),
              book['press'].center(15), str(book['number']).center(15), '|')


def display_borrowed_books(login_user):
    print(' Borrow Information '.center(50, '*'))
    socket_client.sendto(('Books_Borrowed {}'.format(login_user)).encode('utf-8'), address_server)
    borrow_info = json.loads(socket_client.recv(1024).decode('utf-8'))
    print(borrow_info)


def analyze_command(data):
    command_list = (data.strip()).split(b' ')

    # FIXME: 如果数据包含有意料外的空格，将出现 BUG
    # 从后向前，删除空的元素
    # for i in range(len(command_list) - 1, -1, -1):
    #     if command_list[i] == '':
    #         del command_list

    command_bytes = command_list[0]
    parameter_list = command_list[1:]
    return command_bytes, parameter_list


def borrow_book(login_user):
    while True:
        try:
            print(' Borrow Book '.center(50, '*'))
            print('请输入以下信息，用空格分割')
            print('BookID Number')
            borrow_book_id, number = input('').split(' ')
        except 'ValueError':
            print('输入错误，请重新输入')
        except 'TypeError':
            print('类型错误，请重新输入')
        else:
            break
    socket_client.sendto(('Borrow_Book {} {} {}'.format(login_user, borrow_book_id, number)).encode('utf-8'),
                         address_server)
    book_left = int(socket_client.recv(1024).decode('utf-8').split(' ')[1])
    if book_left < 0:
        print('借书失败，还缺 {} 本书，程序返回'.format(abs(book_left)))
    else:
        print('借书成功，还剩下 {} 本书，程序返回'.format(book_left))


def main():
    login_user = login()
    if login_user:
        while True:
            print_main_menu(login_user)
            choice = input('Please input your choice: ')
            if choice == '1':
                display_all_books()
            elif choice == '2':
                display_borrowed_books(login_user)
            elif choice == '3':
                borrow_book(login_user)
            elif choice == '4':
                print('目前版本暂时不能提供服务！')
            elif choice == '0':
                print('系统退出！')
                break
            else:
                print('错误的输入，程序返回！')


if __name__ == '__main__':
    # 初始化网络套接字
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address_server = ('127.0.0.1', 9999)

    main()
