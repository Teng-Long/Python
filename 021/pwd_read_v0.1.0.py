#! python3.6
"""
    作者：杨杰
    功能：读取文件中的密码
    版本：0.1.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：一次性读取文件中的密码
"""


def main():
    # input
    f = open('password_v0.3.0.txt', 'r')
    content = f.read()
    f.close()

    # output
    print(content)


if __name__ == '__main__':
    main()
