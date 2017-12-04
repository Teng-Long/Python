import hashlib
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_sha1(file_url):
    sha1 = hashlib.sha1()
    file = open(file_url, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        sha1.update(buffer)
    file.close()
    return sha1.hexdigest()


def get_file_url():
    if len(sys.argv) != 2:
        file_url = input("Please input the file URL:")
        return file_url
    else:
        return sys.argv[1]


if __name__ == "__main__":
    url = get_file_url()
    print("计算中")
    sha1_hash = get_sha1(url)
    cls()
    print(sha1_hash)
    print("\n")
    input("Press <enter>")
