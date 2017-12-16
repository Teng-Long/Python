#! python3.6


import zlib
import sys
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_crc32(file_url):
    with open(file_url, 'rb') as f:
        return zlib.crc32(f.read())


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
