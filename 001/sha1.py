#! python3.6


import hashlib
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_sha1(file_url):
    sha1_object = hashlib.sha1()
    file_object = open(file_url, 'rb')
    while True:
        buffer = file_object.read(8096)
        if not buffer:
            break
        sha1_object.update(buffer)
    file_object.close()
    return sha1_object.hexdigest()


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
    sha1_hash = []
    print("计算中")
    for i in url:
        sha1_hash.append(get_sha1(remove_quotes(i)))
    cls()
    for i in range(len(sha1_hash)):
        print(remove_quotes(url[i]), "\n", sha1_hash[i], "\n")
    input("Press <enter>")
