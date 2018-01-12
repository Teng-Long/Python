#! python3.6
"""
    作者：杨杰
    功能：数据清洗+可视化（Pandas）
    版本：0.1.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：使用 Pandas 进行数据清洗和数据可视化
"""
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # input
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print(' 基本信息 '.center(50, '*'))
    print(aqi_data.info())
    print(' 数据预览 '.center(50, '*'))
    print(aqi_data.head(5))

    # 数据清洗
    # 清洗规则：AQI > 0
    filter_condition = aqi_data['AQI'] > 0
    cleaned_data = aqi_data[filter_condition]

    # 基本统计
    print(' 基本统计 '.center(50, '*'))
    print('AQI 的最大值', cleaned_data['AQI'].max())
    print('AQI 的最小值', cleaned_data['AQI'].min())
    print('AQI 的平均值', cleaned_data['AQI'].mean())

    # top50
    top50_cities = cleaned_data.sort_values(by=['AQI'], ascending=True).head(50)
    print(' 空气质量指数前 50 '.center(50, '*'))
    print(top50_cities)

    # 数据可视化
    plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置字体为黑体
    plt.rcParams['axes.unicode_minus'] = False      # 设置负号为 False
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量指数最好的 50 个城市', figsize=(19.8, 10.8))
    plt.savefig('top50_aqi_bar.png')

    # output
    plt.show()


if __name__ == '__main__':
    main()
