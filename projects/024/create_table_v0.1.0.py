#! python3.6
"""
    作者：Jason Yang
    功能：创建数据表 create table
    版本：0.1.0
    日期：2018-1-8
    许可证：GPL3+
    0.1.0 新增功能：根据配置文件和初始输入，创建数据表
"""
import json
import pymysql


def read_json(path):
    with open(path, 'r', encoding="utf8") as f:
        content = json.load(f)
        config = content[0]
        return config


def main():
    sql = """CREATE TABLE `books` ()"""
    config = read_json('config.json')
    db = pymysql.connect(**config)
    with db.cursor() as cursor:
        try:
            cursor.execute(sql)
            for line in cursor.fetchall():
                print(', '.join(line))
        except cursor.Error as error:
            print(error)


if __name__ == '__main__':
    main()
