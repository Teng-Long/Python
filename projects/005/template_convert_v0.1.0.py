#! python3.6
"""
    作者：杨杰
    功能：摄氏度与华氏度之间的温度转换
    版本：0.1.0
    日期：2018-1-4
    许可证：GPL3+
    0.1.0 新增功能：摄氏度与华氏度之间的温度转换
"""


def temp_convert():
    val = input("请输入带温度表示符号的温度值(例如：32C): ")
    if val[-1] in ['C', 'c']:
        f = 1.8 * float(val[0:-1]) + 32
        print("转换后的温度为：%.2fF"%f)
        return True
    elif val[-1] in ['F', 'f']:
        c = (float(val[0:-1]) - 32) / 1.8
        print("转换后的温度为：%.2fC" % c)
        return True
    else:
        print("输入有误")
        return False


if __name__ == '__main__':
    while not temp_convert():
        continue
    print("\n")
    input("Press <Enter>")
