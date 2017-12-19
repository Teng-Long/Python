#! python3.6
"""
    作者：杨杰
    功能：汇率转换
    版本：0.3.0
    日期：2017-12-19
    0.2.0 新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
    0.3.0 新增功能：程序可以一直运行，直到用户选择退出
"""

USD_vs_CNY = 6.61244462
currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）：').lower()

while currency_str_value != 'q':
    unit = currency_str_value[-3:]

    if unit == 'cny':
        rmb_str_value = currency_str_value[:-3]
        rmb_value = eval(rmb_str_value)
        usd_value = rmb_value / USD_vs_CNY
        print('美元金额（USD）是：', usd_value)
    elif unit == 'usd':
        usd_str_value = currency_str_value[:-3]
        usd_value = eval(usd_str_value)
        rmb_value = usd_value * USD_vs_CNY
        print('人民币金额（CNY）是：', rmb_value)
    else:
        print('目前版本不支持该种货币')

    print('*' * 50)
    currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）：')

print('程序已退出！')