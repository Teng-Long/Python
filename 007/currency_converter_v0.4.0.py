#! python3.6
"""
    作者：杨杰
    功能：汇率转换
    版本：0.4.0
    日期：2017-12-19
    0.2.0 新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
    0.3.0 新增功能：程序可以一直运行，直到用户选择退出
    0.4.0 新增功能：（1）封装函数（2）使程序结构化
"""


def convert_currency(im, er):
    """
        汇率转换函数
    """
    out = im * er
    return out


def main():
    usd_vs_rmb = 6.61244462
    currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）：').lower()
    unit = currency_str_value[-3:]
    while currency_str_value != 'q':
        if unit == 'cny':
            exchange_rate = 1 / usd_vs_rmb
        elif unit == 'usd':
            exchange_rate = usd_vs_rmb
        else:
            exchange_rate = -1
        if exchange_rate != -1:
            in_money = eval(currency_str_value[:-3])
            out_money = convert_currency(in_money, exchange_rate)
            print('转换后的金额：', out_money)
        else:
            print('不支持该种货币！')
        print('*' * 50)
        currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）：').lower()
    print('程序已退出！')


if __name__ == '__main__':
    main()
