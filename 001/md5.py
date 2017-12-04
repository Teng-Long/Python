import hashlib
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_file_url():
    if len(sys.argv) != 2:
        file_url = input("Please input the file URL:")
        return file_url
    else:
        return sys.argv[1]


def get_md5(file_url):
    md5 = hashlib.md5()
    file = open(file_url, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        md5.update(buffer)
    file.close()
    return md5.hexdigest()


if __name__ == "__main__":
    url = get_file_url()
    print("计算中")
    md5_hash = get_md5(url)
    cls()
    print(md5_hash)
    print("\n")
    input("Press <enter>")
