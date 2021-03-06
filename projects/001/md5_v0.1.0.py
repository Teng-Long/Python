#! python3.6
"""
    作者：杨杰
    功能：计算文件的 MD5
    版本：0.1.0
    日期：2018-1-3
    许可证：GPL3+
    0.1.0 新增功能：拖拽文件或者输入文件路径名，计算文件的 MD5
"""

import hashlib
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_md5(file_url):
    md5_object = hashlib.md5()
    file_object = open(file_url, 'rb')
    while True:
        buffer = file_object.read(8096)
        if not buffer:
            break
        md5_object.update(buffer)
    file_object.close()
    return md5_object.hexdigest()


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
    md5_hash = []
    print("计算中")
    for i in url:
        md5_hash.append(get_md5(remove_quotes(i)))
    cls()
    for i in range(len(md5_hash)):
        print(remove_quotes(url[i]), "\n", md5_hash[i], "\n")
    input("Press <enter>")
