#! python3.6
"""
    作者：杨杰
    功能：返回拖拽文件的路径
    版本：0.1.0
    日期：2018-1-3
    许可证：GPL3+
    0.1.0 新增功能：返回拖拽文件的路径（支持多文件）
"""

import sys


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
    for i in range(len(url)):
        print('{:>14}'.format("file"+str(i)+": "), remove_quotes(url[i]))
    print("\n")
    input("Press <enter>")
