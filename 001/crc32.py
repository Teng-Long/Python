import zlib
import sys
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_crc32(file_url):
    with open(file_url, 'rb') as f:
        return zlib.crc32(f.read())


def get_file_url():
    if len(sys.argv) <= 1:
        file_name = input("Please input the file URL:")
        return file_name
    else:
        return sys.argv[1]


if __name__ == '__main__':
    url = get_file_url()
    print("计算中")
    crc32 = get_crc32(url)
    cls()
    print(crc32)
    print("\n")
    input("Press <Enter>")
