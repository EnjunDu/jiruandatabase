import mysql.connector
from PIL import Image
import io
import csv

# 创建数据库连接
db = mysql.connector.connect(
    host="localhost",  # MySQL服务器地址
    user="root",   # 用户名
    password="2enDSG9byAHJvfx",  # 密码
    database="patient_temperature"  # 数据库名称
)

# 创建游标对象，用于执行SQL查询
cursor = db.cursor()

# 定义表名和 CSV 文件名
n = 1  # 这里可以是任何正整数
table_name = f"patient_temperature{n}"
csv_filename = f"patient_temperature{n}.csv"

# 创建表的 SQL 语句
create_table_query = f"""
CREATE TABLE {table_name} (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT NOT NULL
);
"""

# 执行创建表的 SQL 语句
cursor.execute(create_table_query)

# 打开 CSV 文件并读取数据
with open(csv_filename, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)

    # 遍历每一行并插入到数据库中
    for row in csv_reader:
        temperature = float(row['temperature'])

        # 插入数据的 SQL 语句
        insert_query = f"""
        INSERT INTO {table_name} (temperature)
        VALUES (%s);
        """

        # 执行插入操作
        cursor.execute(insert_query, (temperature,))

# 提交更改
db.commit()

# 关闭连接
cursor.close()
db.close()