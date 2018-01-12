#! python3.6
"""
    作者：杨杰
    功能：网络爬虫
    版本：0.3.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：爬取 http://pm25.in/ 的网页，从网页中提取 AQI
    0.2.0 更新功能：用 beautifulsoap4 改写程序
    0.3.0 新增功能：获取所有城市的 AQI
"""
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
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))

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
    cities_aqi = []

    # 查询 AQI
    for city in cities:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_aqi(city_pinyin)
        print(city_name, city_aqi)

    # output
    print(cities_aqi)


if __name__ == '__main__':
    main()
