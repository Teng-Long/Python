#! python3.6
"""
    作者：杨杰
    功能：对 JSON 文件进行解码
    版本：0.3.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：（1）读取已经获取的 JSON 数据文件
                    （2）将 AQI 前五的数据输出到文件
    0.2.0 新增功能：将 JSON 文件转换为 CSV 文件
    0.3.0 更新功能：根据输入的文件判断是 JSON 格式还是 CSV 格式，并进行相应的操作
"""
import csv
import json

import os


def process_json_file(file_path):
    """
        解码 JSON 文件
    """
    with open(file_path, 'r', encoding='utf8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(file_path):
    """
        解码 CSV 文件
    """
    with open(file_path, 'r', encoding='utf8', newline='') as f:
        city_list = csv.reader(f)
        for line in city_list:
            print(line)
            print(', '.join(line))


def main():
    # input
    file_path = input('请输入 json 文件名称：')
    filename, file_ext = os.path.splitext(file_path)

    if file_ext == '.json':
        process_json_file(file_path)
    elif file_ext == '.csv':
        process_csv_file(file_path)
    else:
        print('不支持的文件格式！')


if __name__ == '__main__':
    main()
