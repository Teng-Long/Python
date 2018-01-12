#! python3.6
"""
    作者：杨杰
    功能：图书馆管理系统（服务端）
    版本：0.5.0
    日期：2017-12-20
    许可证：GPL 3.0
    0.1.0 功能：在服务器创建线程，运行 10s，并输出信息
    0.2.0 新增功能：在管理线程中，运行本地的图书馆管理系统
    0.3.0 新增功能：（1）显示所有书籍（2）合并 main()
    0.4.0 新增功能：用户管理功能
    0.5.0 新增功能：图书管理功能
"""
import threading


def print_main_menu():
    print(' 图书馆管理系统 '.center(50, '*'))
    print('    1: Display all books')
    print('    2: User management')
    print('    3: Book management')
    print('    0: Quit')


def display_all_books():
    print(' Display All Books '.center(50, '*'))
    print('|', 'BookID'.center(15), 'BookName'.center(15), 'Author'.center(15), 'Press'.center(15), 'Number'.center(15),
          '|')
    for book in books:
        print('|', book['book_id'].center(15), book['book_name'].center(15), book['author'].center(15),
              book['press'].center(15), str(book['number']).center(15), '|')


def user_add():
    print(' User Add '.center(50, '*'))
    user_name = input('Please input: ')
    if user_name in users:
        print('用户已存在，程序返回')
    else:
        users.append(user_name)
        print('成功新建用户 {}，程序返回'.format(user_name))


def display_all_users():
    print(' Display All User '.center(50, '*'))
    for user in users:
        print('|', user.center(15), '|')


def user_delete():
    print(' User Delete '.center(50, '*'))
    user_name = input('Please input: ')
    if user_name in users:
        users.remove(user_name)
        if user_name in borrow_info.keys():
            del borrow_info[user_name]
        # FIXME: 借出的书未归还
        print('成功删除用户 {}，程序返回'.format(user_name))
    else:
        print('用户不存在，程序返回')


def user_management():
    while True:
        print(' Users Management '.center(50, '*'))
        print('    1: Display all users')
        print('    2: Add a user')
        print('    3: Delete a user')
        print('    0: Return main menu')
        choice = input('Please input: ')
        if choice == '1':
            display_all_users()
        elif choice == '2':
            user_add()
        elif choice == '3':
            user_delete()
        elif choice == '0':
            break


def book_add():
    print(' Book Add '.center(50, '*'))
    print('请输入以下信息，用空格分割')
    print('BookID    BookName    Author    Press    Number')
    book_info_str = input()
    book_info_str_list = book_info_str.split(' ')
    book_id = book_info_str_list[0]
    book_name = book_info_str_list[1]
    author = book_info_str_list[2]
    press = book_info_str_list[3]
    number = int(book_info_str_list[4])
    # FIXME: 请增加异常处理功能
    books.append({'book_id': book_id, 'book_name': book_name, 'author': author, 'press': press, 'number': number})


def display_borrow_information():
    print(' Borrow Information '.center(50, '*'))
    print(borrow_info)


def book_management():
    while True:
        print(' Books Management '.center(50, '*'))
        print('    1: Display all books')
        print('    2: Display borrow information')
        print('    3: Add a book')
        print('    0: Return main menu')
        choice = input('Please input: ')
        if choice == '1':
            display_all_books()
        elif choice == '2':
            display_borrow_information()
        elif choice == '3':
            book_add()
        elif choice == '0':
            break


def manage_thread():
    print('线程1已运行')
    while True:
        print_main_menu()
        choice = input('Please input: ')
        if choice == '1':
            display_all_books()
        elif choice == '2':
            user_management()
        elif choice == '3':
            book_management()
        elif choice == '0':
            break
        else:
            print('错误的输入，程序返回！')
    print('线程1已停止运行')


def communication_thread():
    pass


if __name__ == '__main__':
    # 初始化变量
    books = [
        {'book_id': 'book001', 'book_name': 'C语言程序设计', 'author': '谭浩强', 'press': '教育出版社', 'number': 5},
        {'book_id': 'book002', 'book_name': '大学国文', 'author': '无名氏', 'press': '教育出版社', 'number': 4},
        {'book_id': 'book003', 'book_name': '计算机科学基础', 'author': '陆汗权', 'press': '电子工业出版社', 'number': 5},
    ]
    users = ['zhang', 'li', 'wang']
    borrow_info = {
        'zhang': {'book001': 1, 'book002': 1},
        'li': {'book001': 1, 'book002': 2},
    }

    # 创建线程，运行线程
    thread_1 = threading.Thread(target=manage_thread, name='Manage Thread')
    thread_2 = threading.Thread(target=communication_thread, name='Communication Thread')
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
