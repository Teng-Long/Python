#! python3.6
"""
    作者：杨杰
    功能：网络爬虫
    版本：0.2.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：爬取 http://pm25.in/ 的网页，从网页中提取 AQI
    0.2.0 更新功能：用 beautifulsoap4 改写程序
"""
import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    """
        获取网页内容
    """
    r = requests.get(url, timeout=30)
    print(r.status_code)
    return r.text


def main():
    # input
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
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
    print(city_aqi)


if __name__ == '__main__':
    main()
