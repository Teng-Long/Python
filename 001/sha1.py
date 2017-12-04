import hashlib
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_sha1(file_name):
    sha1 = hashlib.sha1()
    file = open(file_name, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        sha1.update(buffer)
    file.close()
    return sha1.hexdigest()


def get_file_name():
    if len(sys.argv) != 2:
        filename = input("Please input the file URL:")
        return filename
    else:
        return sys.argv[1]


if __name__ == "__main__":
    file_url = get_file_name()
    print("计算中")
    sha1_hash = get_sha1(file_url)
    cls()
    print(sha1_hash)
    print("\n")
    input("Press <enter>")
