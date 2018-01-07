#! python3.6
"""
    作者：杨杰
    功能：计算空气质量指数
    版本：0.1.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：计算 AQI (Air Quality Index)
"""


def calc_linear(iaqi_low, iaqi_high, bp_low, bp_high, cp):
    """
        线性缩放
    """
    iaqi = (iaqi_high - iaqi_low) * (cp - bp_low) / (bp_high - bp_low) + iaqi_low
    return iaqi


def calc_pm_iaqi(pm_val: str) -> float:
    """
        计算 PM2.5 的 IAQI
    """
    pm_val = float(pm_val)
    pm_iaqi = 0.0
    if 0 <= pm_val < 35:
        pm_iaqi = calc_linear(0, 50, 0, 35, pm_val)
    elif 35 <= pm_val < 75:
        pm_iaqi = calc_linear(50, 100, 35, 75, pm_val)
    elif 75 <= pm_val < 115:
        pm_iaqi = calc_linear(100, 150, 75, 115, pm_val)
    elif 115 <= pm_val < 150:
        pm_iaqi = calc_linear(150, 200, 115, 150, pm_val)
    elif 150 <= pm_val < 250:
        pm_iaqi = calc_linear(200, 300, 150, 250, pm_val)
    elif 250 <= pm_val < 350:
        pm_iaqi = calc_linear(300, 400, 250, 350, pm_val)
    elif 350 <= pm_val < 500:
        pm_iaqi = calc_linear(400, 500, 350, 500, pm_val)
    return pm_iaqi


def calc_co_iaqi(co_val: str) -> float:
    """
        计算 CO 的 IAQI
    """
    co_val = float(co_val)
    co_iaqi = 0.0
    if 0 <= co_val < 2:
        co_iaqi = calc_linear(0, 50, 0, 2, co_val)
    elif 2 <= co_val < 4:
        co_iaqi = calc_linear(50, 100, 2, 4, co_val)
    elif 4 <= co_val < 14:
        co_iaqi = calc_linear(100, 150, 4, 14, co_val)
    elif 14 <= co_val < 24:
        co_iaqi = calc_linear(150, 200, 14, 24, co_val)
    elif 24 <= co_val < 36:
        co_iaqi = calc_linear(200, 300, 24, 36, co_val)
    elif 36 <= co_val < 48:
        co_iaqi = calc_linear(300, 400, 36, 48, co_val)
    elif 48 <= co_val < 60:
        co_iaqi = calc_linear(400, 500, 48, 60, co_val)
    return co_iaqi


def calc_aqi(param_list: list):
    """
        计算 AQI
    """
    # input
    pm_val = param_list[0]
    co_val = param_list[1]

    # 计算 IAQI
    pm_iaqi = calc_pm_iaqi(pm_val)
    co_iaqi = calc_co_iaqi(co_val)

    # 计算 AQI
    iaqi_list = [pm_iaqi, co_iaqi]
    aqi_val = max(iaqi_list)

    # output
    return aqi_val


def main():
    # input
    print('请输入以下信息，用空格分隔')
    input_str = input('(1)PM2.5 (2)CO')
    str_list = input_str.split(' ')
    pm_val = str_list[0]
    co_val = str_list[1]
    param_list = [pm_val, co_val]

    # 计算 AQI
    aqi_val = calc_aqi(param_list)

    # output
    print('空气质量指数为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
