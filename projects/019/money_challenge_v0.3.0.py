#! python3.6
"""
    作者：杨杰
    功能：52 周存钱挑战
    版本：0.3.0
    日期：2018-1-4
    许可证：GPL3+
    0.1.0 新增功能：第一周存 10 元，之后每周递增 10 元，直到第 52 周，共存钱 13780 元
    0.2.0 更新功能：用列表存放每一周存入的钱
    0.3.0 更新功能：用 for 循环替换 while 循环
"""


if __name__ == '__main__':
    # 初始化变量
    money_per_week = 10
    money_increase = 10
    week_total = 52
    money_saving = 0
    money_list = []

    # loop
    for i in range(week_total):
        money_list.append(money_per_week)
        money_saving += money_per_week
        print('第 {} 周，存入 {} 元，账户累计 {} 元'.format(i + 1, money_per_week, money_saving))
        money_per_week += money_increase
