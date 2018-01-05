#! python3.6
"""
    作者：杨杰
    功能：52 周存钱挑战
    版本：0.1.0
    日期：2018-1-4
    许可证：GPL3+
    0.1.0 新增功能：第一周存 10 元，之后每周递增 10 元，直到第 52 周，共存钱 13780 元
    0.2.0 更新功能：用列表存放每一周存入的钱
    0.3.0 更新功能：用 for 循环替换 while 循环
    0.4.0 更新功能：灵活设置每周的存款数，递增的存款数和存款周数
    0.5.0 新增功能：根据用户输入的日期，来判断是一年中的哪一周，然后输入相应的存款金额
"""
import datetime


def save_money_in_n_weeks(money_per_week, money_increase, week_total):
    """
    计算 n 周内的存款金额
    """
    # 初始化变量
    money_saving = 0
    money_list = []
    saved_money_list = []

    # loop
    for i in range(week_total):
        money_list.append(money_per_week)
        money_saving += money_per_week
        saved_money_list.append(money_saving)
        money_per_week += money_increase

    return saved_money_list


def main():
    money_per_week = float(input('请输入第一周存入的金额：'))
    money_increase = float(input('请输入每周递增的金额：'))
    week_total = int(input('请输入总共的周数：'))
    saved_money_list = save_money_in_n_weeks(money_per_week, money_increase, week_total)
    input_date_str = input('请输入日期（yyyy-mm-dd）：')
    date = datetime.datetime.strptime(input_date_str, '%Y-%m-%d')
    week_num = date.isocalendar()[1]
    print('第 {} 周的存款：{} 元'.format(week_num, saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()
