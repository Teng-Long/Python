#! python3.6
"""
    作者：杨杰
    功能：数据分析
    版本：0.1.0
    日期：2018-1-6
    许可证：GPL3+
    0.1.0 新增功能：对 CSV 数据文件进行数据分析
"""
import pandas as pd


def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print(' 基本信息 '.center(50, '*'))
    print(aqi_data.info())
    print(' 数据预览 '.center(50, '*'))
    print(aqi_data.head(5))

    # 基本统计
    print('AQI 的最大值', aqi_data['AQI'].max())
    print('AQI 的最小值', aqi_data['AQI'].min())
    print('AQI 的平均值', aqi_data['AQI'].mean())

    # top10
    top10_cities = aqi_data.sort_values(by=['AQI'], ascending=True).head(10)
    print(top10_cities)

    # bottom10
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print(bottom10_cities)

    # 保存 csv 文件
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('bottom10_aqi.csv', index=False)


if __name__ == '__main__':
    main()
