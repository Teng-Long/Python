#! python3.6
"""
    作者：杨杰
    功能：对 JSON 文件进行解码
    版本：0.2.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：（1）读取已经获取的 JSON 数据文件
                    （2）将 AQI 前五的数据输出到文件
    0.2.0 新增功能：将 JSON 文件转换为 CSV 文件
"""
import csv
import json


def process_json_file(file_path):
    """
        解码 JSON 文件
    """
    f = open(file_path, mode='r', encoding='utf8')
    city_list = json.load(f)
    f.close()
    return city_list


def main():
    # input
    file_path = input('请输入 json 文件名称：')

    # 解码 JSON 文件
    city_list = process_json_file(file_path)

    # 按照 AQI 进行排序
    city_list.sort(key=lambda city: city['aqi'])

    # 提取键名和记录
    lines = [list(city_list[0].keys())]
    for city in city_list:
        lines.append(list(city.values()))

    # output
    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    writer.writerows(lines)
    f.close()


if __name__ == '__main__':
    main()
