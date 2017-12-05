import sys
import os


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
    print("        type: ", type(sys.argv))
    print("         len: ", len(sys.argv))
    for i in range(len(url)):
        print('{:>14}'.format("file"+str(i)+": "), url[i])
    input("Press <enter>")
