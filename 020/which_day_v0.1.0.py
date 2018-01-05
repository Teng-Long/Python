#! python3.6
"""
    作者：杨杰
    功能：判断一个日期是一年中的第几天
    版本：0.1.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：输入某年某月某日，判断这一天是这一年中的第几天
"""
import datetime


def main():
    input_date_str = input('请输入日期（yyyy-mm-dd）：')
    input_date = datetime.datetime.strptime(input_date_str, '%Y-%m-%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_in_month_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_tuple[:month - 1]) + day

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) and month > 2:
        days += 1

    print('这是第 {} 天'.format(days))


if __name__ == '__main__':
    main()
