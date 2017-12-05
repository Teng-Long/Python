import zlib
import sys
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_crc32(file_url):
    crc32_object = zlib.crc32()
    file_object = open(file_url, 'rb')
    while True:
        buffer = file_object.read(8096)
        if not buffer:
            break
        crc32_object.update(buffer)
    file_object.close()
    return crc32_object


def get_file_url():
    if len(sys.argv) != 2:
        file_url = input("Please input the file URL:")
        return file_url
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
