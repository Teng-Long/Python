#! python3.6
"""
    作者：杨杰
    功能：52 周存钱挑战
    版本：0.1.0
    日期：2018-1-4
    许可证：GPL3+
    0.1.0 新增功能：第一周存 10 元，之后每周递增 10 元，直到第 52 周，共存钱 13780 元
"""


if __name__ == '__main__':
    # 初始化变量
    money_per_week = 10
    week_now = 1
    money_increase = 10
    week_total = 52
    money_saving = 0

    # loop
    while week_now <= week_total:
        money_saving += money_per_week
        print('第 {} 周，存入 {} 元，账户累计 {} 元'.format(week_now, money_per_week, money_saving))
        money_per_week += money_increase
        week_now += 1

