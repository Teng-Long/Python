#! python3.6
"""
    作者：杨杰
    功能：判断一个日期是一年中的第几天
    版本：0.4.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：输入某年某月某日，判断这一天是这一年中的第几天
    0.2.0 更新功能：（1）用列表替换元组（2）模块化
    0.3.0 更新功能：将月份划分为不同的集合再操作
    0.4.0 更新功能：将月份及其对应天数通过字典表示
"""
import datetime


def is_leap_year(year):
    """
        判断 year 是否为闰年
        是，返回 True
        否，返回 False
    """
    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True

    return is_leap


def main():
    # input
    input_date_str = input('请输入日期（yyyy-mm-dd）：')
    month_day_dict = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}
    days = 0

    # 得到日期对应的年、月、日
    input_date = datetime.datetime.strptime(input_date_str, '%Y-%m-%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算总天数
    for i in range(1, month):
        days += month_day_dict[i]
    if is_leap_year(year) and month > 2:
        days += 1
    days += day

    # output
    print('这是第 {} 天'.format(days))


if __name__ == '__main__':
    main()
