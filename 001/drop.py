import sys
import os


def get_file_name():
    if len(sys.argv) <= 1:
        file_name = input("Please input the file URL:")
        return file_name
    else:
        return sys.argv[1]


if __name__ == "__main__":
    distinct_url = get_file_name()
    print("        type: ", type(sys.argv))
    print("         len: ", len(sys.argv))
    print("         str: ", str(sys.argv))
    print(" Current_URL: ", sys.argv[0])
    print("Distinct_URL: ", distinct_url)
    input("Press <enter>")
