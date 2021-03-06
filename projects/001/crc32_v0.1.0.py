#! python3.6
"""
    作者：杨杰
    功能：计算文件的 crc32
    版本：0.1.0
    日期：2018-1-3
    许可证：GPL3+
    0.1.0 新增功能：拖拽文件或者输入文件路径名，计算文件的 crc32
"""

import zlib
import sys
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_crc32(file_url):
    with open(file_url, 'rb') as file_object:
        return zlib.crc32(file_object.read())


def get_file_url():
    if len(sys.argv) == 1:
        file_name = input("Please input the file URL:")
        return [file_name]
    elif len(sys.argv) == 2:
        return [sys.argv[1]]
    else:
        return sys.argv[1:]


def remove_quotes(string_object):
    return string_object.strip('"')


if __name__ == "__main__":
    url = get_file_url()
    crc32_hash = []
    print("计算中")
    for i in url:
        crc32_hash.append(get_crc32(remove_quotes(i)))
    cls()
    for i in range(len(crc32_hash)):
        print(remove_quotes(url[i]), "\n", crc32_hash[i], "\n")
    input("Press <enter>")
