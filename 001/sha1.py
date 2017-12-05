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
    if len(sys.argv) == 1:
        file_name = input("Please input the file URL:")
        return [file_name]
    elif len(sys.argv) == 2:
        return [sys.argv[1]]
    else:
        return sys.argv[1:]


if __name__ == "__main__":
    url = get_file_url()
    sha1_hash = []
    print("计算中")
    for i in url:
        sha1_hash.append(get_sha1(i))
    cls()
    for i in range(len(sha1_hash)):
        print(url[i], "\n", sha1_hash[i], "\n")
    input("Press <enter>")
