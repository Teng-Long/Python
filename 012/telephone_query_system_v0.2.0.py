#! python3.6
# coding=utf-8
"""
    作者：杨杰
    功能：号码归属地查询系统
    版本：0.2.0
    日期：2017-12-21
    许可证：GPL3.0
    0.1.0 发布功能：号码归属地查询系统
    0.2.0 版本变化：对代码的结构进行修改
"""

import urllib.request
import urllib.response
import json


def print_main_menu():
    print(' 号码归属地查询系统 '.center(50, '*'))
    print('    1: 查询号码归属地')
    print('    0: quit')


def query_telephone_number(tel_num):
    """
        查询号码归属地，并在屏幕上打印相关信息
    """
    host = 'http://jshmgsdmfb.market.alicloudapi.com'
    path = '/shouji/query'
    method = 'GET'
    app_code = '07bad8b77afe474191ff4212fdb910bc'
    query = 'shouji=' + tel_num
    # bodys = {}
    url = host + path + '?' + query
    request = urllib.request.Request(url, method=method)
    request.add_header('Authorization', 'APPCODE ' + app_code)
    response = urllib.request.urlopen(request)
    content_str = response.read()

    # 编码、解码，然后由字符串转为字典
    content_dict = json.loads(urllib.request.unquote(urllib.request.quote(content_str)))

    if content_dict:
        print('{:>18}{}'.format('　　　手机：', content_dict["result"]["shouji"]))
        print('{:>18}{}'.format('　所在省份：', content_dict["result"]["province"]))
        print('{:>18}{}'.format('　所在城市：', content_dict["result"]["city"]))
        print('{:>18}{}'.format('　　运营商：', content_dict["result"]["company"]))
        print('{:>18}{}'.format('手机卡类型：', content_dict["result"]["cardtype"]))
        print('{:>18}{}'.format('　　　区号：', content_dict["result"]["areacode"]))


if __name__ == '__main__':
    while True:
        print_main_menu()
        choice = input('Please input your choice: ')
        if choice == '1':
            telephone_number = input('Please input your telephone number: ')
            query_telephone_number(telephone_number)
        elif choice == '0':
            exit(code=0)
