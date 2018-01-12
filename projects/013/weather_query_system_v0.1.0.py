#! python3.6
# coding=utf-8
"""
    作者：杨杰
    功能：全国天气预报查询系统
    版本：0.1.0
    日期：2017-12-21
    许可证：GPL3.0
    0.1.0 新增功能：全国天气预报查询系统
"""

import urllib.request
import urllib.response
import json


def main():
    """
        主程序
    """
    while True:
        print_main_menu()
        choice = eval(input('Please input your choice: '))
        if choice == 1:
            city_name_str = input('Please input your city: ')
            city_name = urllib.request.quote(city_name_str)
            query_weather(city_name)
        elif choice == 0:
            break


def print_main_menu():
    """
        在屏幕上打印主菜单
    """
    print('-' * 20, '全国天气预报查询系统', '-' * 20)
    print('    1: 查询天气预报')
    print('    0: quit')


def query_weather(cn):
    """
        查询天气预报，并在屏幕上打印相关信息
    """
    host = 'http://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    # method = 'GET'
    app_code = '07bad8b77afe474191ff4212fdb910bc'
    query = 'city=' + cn
    # bodys = {}
    url = host + path + '?' + query
    request = urllib.request.Request(url)
    request.add_header('Authorization', 'APPCODE ' + app_code)
    response = urllib.request.urlopen(request)
    content_str = response.read()
    content_dict = json.loads(urllib.request.unquote(urllib.request.quote(content_str)))
    print(content_dict)
    if content_dict:
        print('{:>18}{}'.format('　　　　城市：', content_dict["result"]["city"]))
        print('{:>18}{}'.format('　　　　日期：', content_dict["result"]["date"]))
        print('{:>18}{}'.format('　　　　星期：', content_dict["result"]["week"]))
        print('{:>18}{}'.format('　　　　天气：', content_dict["result"]["weather"]))
        print('{:>18}{}'.format('　　当前气温：', content_dict["result"]["temp"]))
        print('{:>18}{}'.format('　　　最高温：', content_dict["result"]["temphigh"]))
        print('{:>18}{}'.format('　　　最低温：', content_dict["result"]["templow"]))
        print('{:>18}{}'.format('　　　　湿度：', content_dict["result"]["humidity"]))
        print('{:>18}{}'.format('　　　　气压：', content_dict["result"]["pressure"]))
        print('{:>18}{}'.format('　　　　风速：', content_dict["result"]["windspeed"]))
        print('{:>18}{}'.format('　　　　风向：', content_dict["result"]["winddirect"]))
        print('{:>18}{}'.format('　　　　风级：', content_dict["result"]["windpower"]))
        print('{:>18}{}'.format('　　更新时间：', content_dict["result"]["updatetime"]))
        print('{:>18}{}'.format('空气污染指数：', content_dict["result"]["index"][5]["ivalue"]))
        print('{:>18}{}'.format('　　指数详情：', content_dict["result"]["index"][5]["ivalue"]))
        print('{:>24}{}'.format('       PM2.5：', content_dict["result"]["aqi"]["pm2_5"]))


if __name__ == '__main__':
    main()
