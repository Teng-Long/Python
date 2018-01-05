#! python3.6
"""
    作者：杨杰
    功能：对 JSON 文件进行解码
    版本：0.1.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：（1）读取已经获取的 JSON 数据文件
                    （2）将 AQI 前五的数据输出到文件
"""
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

    # 取得 AQI 前五的数据
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]

    # 编码为 JSON 格式
    # output
    f = open('top5_aqi.json', mode='w', encoding='utf8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
