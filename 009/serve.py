#! python3.6
"""
新增功能：（1）网络命令用逗号代替空格（2）修复数据包含有意料外的空格导致的BUG（3）使用数据库查找用户
"""
import socket
import threading

import pymysql.cursors


def analyze_command(data):
    command_list = data.split(b',')
    for i in range(len(command_list) - 1, -1, -1):
        command_list[i] = command_list[i].strip()
        if command_list[i] == b'':
            del command_list
    command_bytes = command_list[0]
    parameter_list = command_list[1:]
    return command_bytes, parameter_list


def users_list():
    """
    以列表形式返回数据库中的 users
    :return:
    """
    database_connection = pymysql.connect(**config)
    with database_connection.cursor() as cursor:
        try:
            sql = 'select `user` from users'
            cursor.execute(sql)
            select_result = cursor.fetchall()
            users = []
            for user in select_result:
                users.append(user['user'])
            return users
        finally:
            database_connection.close()


def client_login(parameter_list, address_client):
    if parameter_list[0].decode('utf-8') in users_list():
        socket_server.sendto(b'LoginResponse OK', address_client)
        print('登录成功')
    else:
        socket_server.sendto(b'LoginResponse FAIL', address_client)
        print('登录失败')


def execute_command(command_bytes, parameter_list, address_client):
    print(' Log Console '.center(50, '*'))
    if command_bytes == b'Login':
        print('用户登录：{} '.format(parameter_list[0].decode()))
        client_login(parameter_list, address_client)


def communication_thread():
    while True:
        data, address_client = socket_server.recvfrom(buffer_size)
        command_bytes, parameter_list = analyze_command(data)
        execute_command(command_bytes, parameter_list, address_client)


if __name__ == '__main__':
    address_server = ('127.0.0.1', 9999)
    buffer_size = 1024
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server.bind(address_server)

    config = {
        'host': '39.108.85.208',
        'user': 'jason',
        'password': '19990124**1y',
        'db': 'jason_library_system',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
        }

    thread_1 = threading.Thread(target=communication_thread, name="Communication Thread")
    thread_1.start()
    thread_1.join()
