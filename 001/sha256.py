import hashlib
import os
import sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def sha256(file_name):
    sha256hash = hashlib.sha256()
    file = open(file_name, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        sha256hash.update(buffer)
    file.close()
    return(sha256hash.hexdigest())

def get_file_name():
    if len(sys.argv)!=2:
        filename = input("Please input the file URL:")
        return filename
    else:
        return sys.argv[1]

if __name__ == "__main__":
    file_name = get_file_name()
    print("计算中")
    sha256hash = sha256(file_name)
    cls()
    print(sha256hash)
    print("\n")
    input("Press <enter>")


