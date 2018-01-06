#! python3.6
"""
    作者：杨杰
    功能：网络爬虫
    版本：0.1.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：整合 json_v0.3.0.py web_crawler_v0.3.0.py，将所有城市空气质量指数保存为 CSV 数据文件
"""
import csv

import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    """
        获取网页内容
    """
    r = requests.get(url, timeout=30)
    return r.text


def get_city_aqi(city):
    # input
    url = 'http://pm25.in/' + city
    city_aqi = []

    # 获取网页内容
    url_text = get_html_text(url)

    # 查找节点
    bs = BeautifulSoup(url_text, 'lxml')
    div_list = bs.find_all('div', {'class': 'span1'})
    for div_content in div_list[:8]:
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append(value)

    # output
    return city_aqi


def get_all_cities():
    # input
    url = 'http://pm25.in/'
    city_list = []

    # 获取网页内容
    url_text = get_html_text(url)

    # 查找节点
    bs = BeautifulSoup(url_text, 'lxml')
    div_list = bs.find_all('div', {'class': 'bottom'})[1]
    city_link_list = div_list.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'].lstrip('/')
        city_list.append((city_name, city_pinyin))

    # output
    return city_list


def main():
    # input
    cities = get_all_cities()
    cities_total_num = len(cities)
    header = ['City', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']

    # output
    with open('china_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        for i, city in enumerate(cities):
            if (i + 1) % 10 == 0:
                print('正在处理 {:0>3}/{:0>3}'.format(i + 1, cities_total_num))
            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row = [city_name] + city_aqi
            csv_writer.writerow(row)
    print()
    print('任务已完成！')


if __name__ == '__main__':
    main()
