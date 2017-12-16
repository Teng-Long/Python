#! python3.6


import hashlib
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    md5_hash = []
    print("计算中")
    for i in url:
        md5_hash.append(get_md5(remove_quotes(i)))
    cls()
    for i in range(len(md5_hash)):
        print(remove_quotes(url[i]), "\n", md5_hash[i], "\n")
    input("Press <enter>")
