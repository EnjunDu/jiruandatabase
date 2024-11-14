import os

def remove_null_bytes(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        if b'\x00' in content:
            print(f"Null byte found in: {file_path}")
            new_content = content.replace(b'\x00', b'')
            with open(file_path, 'wb') as f:
                f.write(new_content)
            print(f"Null byte removed from: {file_path}")
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")

# 指定生成的模型文件路径
file_path = 'D:/JiRuan_Projects/database_for_jiruan/MedicDataBase/Data_Manage/models.py'
remove_null_bytes(file_path)