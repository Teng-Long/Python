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


def get_sha256(file_url):
    sha256 = hashlib.sha1()
    file = open(file_url, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        sha256.update(buffer)
    file.close()
    return sha256.hexdigest()


if __name__ == "__main__":
    url = get_file_url()
    print("计算中")
    sha256_hash = get_sha256(url)
    cls()
    print(sha256_hash)
    print("\n")
    input("Press <enter>")
