import hashlib
import os
import sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def md5(file_name):
    md5hash = hashlib.md5()
    file = open(file_name, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        md5hash.update(buffer)
    file.close()
    return(md5hash.hexdigest())

def get_file_name():
    if len(sys.argv)!=2:
        filename = input("Please input the file URL:")
        return filename
    else:
        return sys.argv[1]

if __name__ == "__main__":
    file_name = get_file_name()
    print("计算中")
    md5hash = md5(file_name)
    cls()
    print(md5hash)
    print("\n")
    input("Press <enter>")
