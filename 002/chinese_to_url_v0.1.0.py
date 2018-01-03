#! python3.6
"""
    作者：杨杰
    功能：将中文转码为 url
    版本：0.1.0
    日期：2018-1-3
    许可证：GPL3+
    0.1.0 新增功能：（1）将中文转码为 url（2）将 url 转为中文
"""
from urllib.parse import quote
from urllib.parse import unquote


def print_main_menu():
    print(' Main Menu '.center(50, '*'))
    print('    1: 将中文转码为 url')
    print('    2: 将 url 转码为中文')
    print('    0: 退出')


def chinese_to_url():
    print(' Chinese to Url '.center(50, '*'))
    string_chinese = input('Please input: ')
    string_url = quote(string_chinese, safe='/:?=&+')
    print('转码结果：{}'.format(string_url))
    print('程序返回！')


def url_to_chinese():
    print(' Url to Chinese '.center(50, '*'))
    string_chinese = input('Please input: ')
    string_url = unquote(string_chinese)
    print('转码结果：{}'.format(string_url))
    print('程序返回！')


if __name__ == '__main__':
    while True:
        print_main_menu()
        choice = input('Please input: ')
        if choice == '1':
            chinese_to_url()
        elif choice == '2':
            url_to_chinese()
        elif choice == '0':
            break
