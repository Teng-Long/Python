#! python3.6
"""
    作者：杨杰
    功能：将中文转码为 url
    版本：0.1.0
    日期：2018-1-3
    许可证：GPL3+
    0.1.0 新增功能：（1）将中文转码为 url（2）将 url 解码
"""
from urllib.parse import quote
from urllib.parse import unquote


def print_main_menu():
    print(' Main Menu '.center(50, '*'))
    print('    1: 将中文转码为 url')
    print('    2: 将 url 解码')
    print('    0: 退出')


def chinese_to_url():
    """
    编码器
    """
    print(' Chinese to Url '.center(50, '*'))
    string_chinese = input('Please input: ')
    string_url = quote(string_chinese, safe='/:?=&+')
    print('转码结果：{}'.format(string_url))
    print('程序返回！')


def url_unquote():
    """
    解码器
    """
    print(' Url to Chinese '.center(50, '*'))
    string_url = input('Please input: ')
    string_unquote = unquote(string_url)
    print('转码结果：{}'.format(string_unquote))
    print('程序返回！')


if __name__ == '__main__':
    while True:
        print_main_menu()
        choice = input('Please input: ')
        if choice == '1':
            chinese_to_url()
        elif choice == '2':
            url_unquote()
        elif choice == '0':
            break
