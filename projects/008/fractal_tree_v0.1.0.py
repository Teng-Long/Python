#! python3.6
"""
    作者：杨杰
    功能：绘制分形树
    版本：0.1.0
    日期：2017-12-19
    许可证：GPL 3.0
    0.1.0 新增功能：利用递归函数绘制分形树
"""


import turtle


def draw_braches(branch_lench):
    """
        绘制分形树
    """
    if branch_lench >= 15:
        # 绘制右侧树枝
        turtle.forward(branch_lench)
        turtle.right(25)
        draw_braches(branch_lench - 20)

        # 绘制左侧树枝
        turtle.left(50)
        draw_braches(branch_lench - 20)

        # 返回之前的树枝
        turtle.right(25)
        if branch_lench <= 30:
            turtle.colormode(255)
            turtle.pencolor(30, 205, 30)
            turtle.back(branch_lench)
            turtle.pencolor('brown')
        else:
            turtle.back(branch_lench)


def main():
    """
        主函数
    """
    # turtle.tracer(False)
    turtle.up()
    turtle.left(90)
    turtle.speed(8)
    turtle.back(300)
    turtle.pencolor('brown')
    turtle.pensize(2)
    turtle.down()
    draw_braches(150)
    turtle.tracer(True)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
