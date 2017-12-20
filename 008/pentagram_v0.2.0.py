#! python3.6
"""
    作者：杨杰
    功能：绘制五角星
    版本：0.2.0
    日期：2017-12-19
    许可证：GPL 3.0
    0.2.0 新增功能：加入循环操作绘制重复不同大小的五角星
"""


import turtle


def draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    turtle.penup()
    turtle.back(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')
    size = 50
    while size <= 100:
        draw_pentagram(size)
        size += 10
    turtle.exitonclick()


if __name__ == '__main__':
    main()
