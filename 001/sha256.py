#! python3.6


import hashlib
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_sha256(file_url):
    sha256 = hashlib.sha256()
    file = open(file_url, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        sha256.update(buffer)
    file.close()
    return sha256.hexdigest()


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
    sha256_hash = []
    print("计算中")
    for i in url:
        sha256_hash.append(get_sha256(remove_quotes(i)))
    cls()
    for i in range(len(sha256_hash)):
        print(remove_quotes(url[i]), "\n", sha256_hash[i], "\n")
    input("Press <enter>")
