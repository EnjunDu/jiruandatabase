import pymysql
import random
import string
from datetime import datetime, timedelta
import os

# 连接到 MySQL 数据库
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="2enDSG9byAHJvfx",
    database="medicaldata",
    charset="utf8mb4"
)

cursor = connection.cursor()

# 工具函数：生成随机字符串
def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# 工具函数：生成随机日期
def random_date(start_year=1950, end_year=2023):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# 工具函数：生成随机电话号码
def random_phone_number():
    return ''.join(random.choice(string.digits) for i in range(10))

# 工具函数：生成随机地址
def random_address():
    return f"{random.randint(1, 9999)} {random_string(10)} St"

# 插入随机数据到各表
try:
    # 1. 插入 Patient 数据
    for _ in range(9):
        cursor.execute("""
            INSERT INTO Patient (Name, Gender, DateOfBirth, ContactInfo, Address)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            random_string(10),
            random.choice(['Male', 'Female', 'Other']),
            random_date(),
            random_phone_number(),
            random_address()
        ))

    # 其他插入数据的代码...

    # 提交更改并关闭连接
    connection.commit()
    print("数据已成功插入。")

except Exception as e:
    print(f"发生错误：{e}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()
