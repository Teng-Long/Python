#! python3.6
"""
    作者：杨杰
    功能：网络爬虫
    版本：0.1.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：爬取 http://pm25.in/ 的网页，从网页中提取 AQI
"""
import requests


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

    # 获取网页内容
    url_text = get_html_text(url)

    # 提取 AQI
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    aqi_index = url_text.find(aqi_div)
    begin_index = aqi_index + len(aqi_div)
    aqi_val_str = ''
    for i in url_text[begin_index:]:
        if i.isnumeric():
            aqi_val_str += i
        else:
            break

    # output
    print('空气质量指数为：{}'.format(aqi_val_str))


if __name__ == '__main__':
    main()
