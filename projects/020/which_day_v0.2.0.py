#! python3.6
"""
    作者：杨杰
    功能：判断一个日期是一年中的第几天
    版本：0.2.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：输入某年某月某日，判断这一天是这一年中的第几天
    0.2.0 更新功能：（1）用列表替换元组（2）模块化
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
    input_date_str = input('请输入日期（yyyy-mm-dd）：')
    input_date = datetime.datetime.strptime(input_date_str, '%Y-%m-%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month_list[1] = 29
    days = sum(days_in_month_list[:month - 1]) + day

    print('这是第 {} 天'.format(days))


if __name__ == '__main__':
    main()
