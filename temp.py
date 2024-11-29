import mysql.connector

def fetch_temperature_data():
    # 连接到Medicaldata数据库
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='2enDSG9byAHJvfx',
        database='Medicaldata'
    )
    cursor = conn.cursor()

    try:

        # 查询Temperature数据
        cursor.execute("SELECT * FROM Temperature")
        data = cursor.fetchall()

    except Exception as e:
        print(f"An error occurred: {e}")

    
    # 关闭数据库连接
    conn.close()
    
    return data

def write_to_file(data):
    with open('otp.txt', 'w') as file:
        for row in data:
            file.write(f"{row}\n")

if __name__ == "__main__":
    temperature_data = fetch_temperature_data()
    write_to_file(temperature_data)
