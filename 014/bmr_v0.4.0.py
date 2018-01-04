#! python3.6
"""
    作者：杨杰
    功能：计算 BMR
    版本：0.3.0
    日期：2018-1-4
    许可证：GPL3.0
    0.1.0 新增功能：计算 BMR
    0.2.0 新增功能：根据用户的输入计算 BMR，程序持续运行，直到用户选择退出
    0.3.0 新增功能：（1）用户可以在一行内输入所有信息（2）带单位的信息输出
    0.4.0 更新功能：更优雅的异常处理机制
"""


def bmr():
    print(' BMR 计算器 '.center(50, '*'))
    print('请输入以下信息，用空格分割')
    print('性别 体重(kg) 身高(cm) 年龄')
    try:
        info_str = input('')
        info_str_list = info_str.split(' ')
        gender = info_str_list[0]
        weight = float(info_str_list[1])
        height = float(info_str_list[2])
        age = int(info_str_list[3])

        # 基础代谢率（Basic Metabolic Rate）指人在安静状态（通常是静卧）下消耗的最低热量
        # BMR 的单位是 千焦/平方米/小时
        # BMR(男) = (13.7 * 体重) + (5.0 * 身高) - (6.8 * 年龄) + 66
        # BMR(女) = (9.6 * 体重) + (1.8 * 身高) - (4.7 * 年龄) + 655
        if gender in gender_words_male:
            bmr_result = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        else:
            bmr_result = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655

        print('基础代谢率：{}大卡'.format(bmr_result))
    except ValueError:
        print('请输入正确的信息！')
        print('程序返回！')
    except IndexError:
        print('输入的信息过少！')
        print('程序返回！')
    else:
        print('程序异常！')
        print('程序返回！')


def print_main_menu():
    print(' 主菜单 '.center(50, '*'))
    print('    1: 开始计算 BMR')
    print('    0: 退出')


if __name__ == '__main__':
    gender_words_male = ['male', '男', 'Male', 'MALE', 'nan']
    gender_words_female = ['female', '女', 'Female', 'FEMALE', 'nv']
    while True:
        print_main_menu()
        selection = input('Press input: ')
        if selection == '1':
            bmr()
            continue
        elif selection == '0':
            break
        else:
            continue
