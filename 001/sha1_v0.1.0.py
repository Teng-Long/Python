#! python3.6
"""
    作者：杨杰
    功能：计算文件的 SHA1
    版本：0.1.0
    日期：2018-1-3
    许可证：GPL3+
    0.1.0 新增功能：拖拽文件或者输入文件路径名，计算文件的 SHA1
"""


import hashlib
import os
import sys


def cls():
    """
    清屏
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_sha1(file_url):
    """
    计算文件的 SHA1
    """
    sha1_object = hashlib.sha1()
    file_object = open(file_url, 'rb')
    while True:
        buffer = file_object.read(8096)
        if not buffer:
            break
        sha1_object.update(buffer)
    file_object.close()
    return sha1_object.hexdigest()
    # 写法二
    # from hashlib import sha1
    #
    #
    # def get_sha1(file_url):
    #     sha1_object = sha1()
    #     with open(file_url, 'rb') as f:
    #         sha1_object.update(f.read())
    #     return sha1_object.hexdigest()


def get_file_url():
    """
    使用 sys.argv 取得拖拽文件的路径，返回值类型为列表
    """
    if len(sys.argv) == 1:
        file_name = input("Please input the file URL:")
        return [file_name]
    elif len(sys.argv) == 2:
        return [sys.argv[1]]
    else:
        return sys.argv[1:]


def remove_quotes(string_object):
    """
    去除字符串首尾的半角双引号
    """
    return string_object.strip('"')


if __name__ == "__main__":
    url = get_file_url()
    sha1_hash = []
    print("计算中")
    for i in url:
        sha1_hash.append(get_sha1(remove_quotes(i)))
    cls()
    for i in range(len(sha1_hash)):
        print(remove_quotes(url[i]), "\n", sha1_hash[i], "\n")
    input("Press <enter>")
