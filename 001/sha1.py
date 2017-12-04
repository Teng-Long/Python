import hashlib
import os
import sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def sha1(file_name):
    sha1hash = hashlib.sha1()
    file = open(file_name, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        sha1hash.update(buffer)
    file.close()
    return(sha1hash.hexdigest())

def get_file_name():
    if len(sys.argv)!=2:
        filename = input("Please input the file URL:")
        return filename
    else:
        return sys.argv[1]

if __name__ == "__main__":
    file_name = get_file_name()
    print("计算中")
    sha1hash = sha1(file_name)
    cls()
    print(sha1hash)
    print("\n")
    input("Press <enter>")


