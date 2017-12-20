#! python3.6
"""
    作者：杨杰
    功能：绘制五角星
    版本：0.1.0
    日期：2017-12-19
    许可证：GPL 3.0
"""


import turtle


def main():
    count = 1
    while count <= 5:
        turtle.forward(100)
        turtle.right(144)
        count += 1
    turtle.exitonclick()


if __name__ == '__main__':
    main()
