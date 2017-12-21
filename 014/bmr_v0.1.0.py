#! python3.6
"""
    作者：杨杰
    功能：计算 BMR
    版本：0.1.0
    日期：2017-12-21
    许可证：GPL3.0
"""


def main():
    """
    主函数
    """
    # 初始化输入，采用单位是 kg 和 cm
    gender = 'male'
    weight = 70
    height = 175
    age = 25

    # BMR 公式：
    # BMR(男) = (13.7 * 体重) + (5.0 * 身高) - (6.8 * 年龄) + 66
    # BMR(女) = (9.6 * 体重) + (1.8 * 身高) - (4.7 * 年龄) + 655
    if gender in ['male', '男', 'Male', 'MALE']:
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender in ['female', '女', 'Female', 'FEMALE']:
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
    else:
        bmr = -1

    # 输出
    if bmr != -1:
        print('基础代谢率（大卡）：', bmr)
    else:
        print('暂不支持该性别')


if __name__ == '__main__':
    main()
