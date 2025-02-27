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
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

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

# 工具函数：生成随机二进制数据
def random_binary_data(size=256):
    return bytes(random.getrandbits(8) for _ in range(size))

# 读取二进制文件
def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return binary_data

try:
    # 插入 Temperature 数据
    cursor.execute("SELECT PatientID FROM Patient")
    patient_ids = [row[0] for row in cursor.fetchall()]
    for _ in range(10):  # 插入10条数据
        cursor.execute("""
            INSERT INTO Temperature (PatientID, ImageType, ImagePath, TemperatureImage, RecordDate)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            random.choice(patient_ids),
            'Prediction',
            r'D:\JiRuan_Projects\database_for_jiruan\Predictions\BloodPressure\patient_blood_pressure1.png',
            read_binary_file(r'D:\JiRuan_Projects\database_for_jiruan\Predictions\BloodPressure\patient_blood_pressure1.png'),
            random_date()
        ))

    # 提交更改并关闭连接
    connection.commit()
    print("Temperature数据已成功插入。")

except Exception as e:
    print(f"发生错误：{e}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()