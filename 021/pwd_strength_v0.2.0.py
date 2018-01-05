#! python3.6
"""
    作者：杨杰
    功能：判断密码强弱
    版本：0.2.0
    日期：2018-1-5
    许可证：GPL3+
    0.1.0 新增功能：设置一个变量 strength_level 用于几率密码的强弱，初始为 0，每满足一个条件，加 1
                    长度判断，使用 len() 方法
                    包含数字判断，使用 isnumeric() 方法
                    包含字母判断，使用 isalpha() 方法
                    如果 strength_level 等于3，密码强度合格，否则不合格
    0.2.0 新增功能：（1）限制密码设置次数；
                    （2）循环的终止
"""


def check_number_exist(pwd_str):
    """
        判断字符串中是否含有数字
        是，返回 True
        否，返回 False
    """
    exist_number = False
    for c in pwd_str:
        if c.isnumeric():
            exist_number = True
            break
    return exist_number


def check_letter_exist(pwd_str):
    """
        判断字符串中是否含有字母
        是，返回 True
        否，返回 False
    """
    exist_letter = False
    for c in pwd_str:
        if c.isalpha():
            exist_letter = True
            break
    return exist_letter


def main():
    # 设置最多尝试次数为 5
    try_times = 5
    while try_times > 0:
        # input
        password = input('请输入密码：')
        strength_level = 0

        # 规则 1：密码长度大于等于 8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少 8 位！')

        # 规则 2：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则 3：包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')

        # output
        if strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('抱歉！密码强度不合格！')
            try_times -= 1
        print()

    if try_times == 0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()
