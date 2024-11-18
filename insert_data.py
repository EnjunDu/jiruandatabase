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

# 插入随机数据到各表
try:
    # 1. 插入 Patient 数据
    for _ in range(1):
        cursor.execute("""
            INSERT INTO Patient (Name, Gender, DateOfBirth, ContactInfo, Address)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            'John Doe',
            'Male',
            '1980-01-01',
            '1234567890',
            '123 Main St'
        ))
    
    # 2. 插入 Doctor 数据
    for _ in range(1):
        cursor.execute("""
            INSERT INTO Doctor (Name, Specialty, ContactInfo, Department)
            VALUES (%s, %s, %s, %s)
        """, (
            'Dr. Smith',
            'Cardiology',
            '0987654321',
            'Cardiology'
        ))

    # 3. 插入 Hospital 数据
    for _ in range(1):
        cursor.execute("""
            INSERT INTO Hospital (HospitalName, Address, ContactInfo)
            VALUES (%s, %s, %s)
        """, (
            'General Hospital',
            '456 Elm St',
            '1122334455'
        )) 

    # 4. 插入 Department 数据
    cursor.execute("SELECT HospitalID FROM Hospital")
    hospital_ids = [row[0] for row in cursor.fetchall()]
    for _ in range(1):
        cursor.execute("""
            INSERT INTO Department (DepartmentName, HospitalID)
            VALUES (%s, %s)
        """, (
            'Emergency',
            random.choice(hospital_ids)
        ))

    # 5. 插入 MedicalRecord 数据
    cursor.execute("SELECT PatientID FROM Patient")
    patient_ids = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT DoctorID FROM Doctor")
    doctor_ids = [row[0] for row in cursor.fetchall()]
    for _ in range(1):
        cursor.execute("""
            INSERT INTO MedicalRecord (PatientID, DoctorID, DiagnosisDate, DiagnosisResult, Prescription)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            random.choice(patient_ids),
            random.choice(doctor_ids),
            '2023-01-01',
            read_binary_file(r'medicaldata/MedicalRecord/DiagnosisResult1.pdf'),
            read_binary_file(r'medicaldata\MedicalRecord\Prescription1.pdf')
        ))

    # 6. 插入 MedicalImage 数据
    cursor.execute("SELECT RecordID FROM MedicalRecord")
    record_ids = [row[0] for row in cursor.fetchall()]
    for _ in range(1):
        cursor.execute("""
            INSERT INTO MedicalImage (RecordID, ImageType, StoragePath, UploadDate, CTImage, MRIImage, UltrasoundImage)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            random.choice(record_ids),
            'CT',
            r'medicaldata\MedicalImage\CTImage1.jpg',
            '2023-01-01',
            read_binary_file(r'medicaldata\MedicalImage\CTImage1.jpg'),
            read_binary_file(r'medicaldata\MedicalImage\MRIImage1.bmp'),
            read_binary_file(r'medicaldata\MedicalImage\UltrasoundImage1.png')
        ))

    # 7. 插入 GenomicData 数据
    for _ in range(1):
        cursor.execute("""
            INSERT INTO GenomicData (PatientID, GeneSequence, AnalysisResult)
            VALUES (%s, %s, %s)
        """, (
            random.choice(patient_ids),
            read_binary_file(r'medicaldata\GenomicData\GeneSequence1.fasta'),
            read_binary_file(r'medicaldata\GenomicData\AnalysisResult1.pdf')
        ))

    # 8. 插入 DeviceData 数据
    for _ in range(1):
        cursor.execute("""
            INSERT INTO DeviceData (PatientID, DeviceType, DataContent, RecordDate)
            VALUES (%s, %s, %s, %s)
        """, (
            random.choice(patient_ids),
            'HeartMonitor',
            read_binary_file(r'medicaldata\DeviceData\DataContent1.pdf'),
            '2023-01-01'
        ))

    # 9. 插入 AudioRecord 数据
    for _ in range(1):
        cursor.execute("""
            INSERT INTO AudioRecord (CounselingAudio, PostOpCareAudio, ConditionChangeAudio)
            VALUES (%s, %s, %s)
        """, (
            read_binary_file(r'medicaldata\AudioRecord\CounselingAudio1.mp3'),
            read_binary_file(r'medicaldata\AudioRecord\PostOpCareAudio1.mp3'),
            read_binary_file(r'medicaldata\AudioRecord\ConditionChangeAudio1.mp3')
        ))

    # 10. 插入 Document 数据
    for _ in range(1):
        cursor.execute("""
            INSERT INTO Document (AdmissionRecord, DischargeSummary, TreatmentPlan)
            VALUES (%s, %s, %s)
        """, (
            read_binary_file(r'medicaldata\Document\AdmissionRecord1.pdf'),
            read_binary_file(r'medicaldata\Document\DischargeSummary1.pdf'),
            read_binary_file(r'medicaldata\Document\TreatmentPlan1.pdf')
        ))

    # 11. 插入 StandardVideo 数据
    for _ in range(1):
        cursor.execute("""
            INSERT INTO StandardVideo (SurgicalProcedureVideo, NursingStandardVideo, EmergencyProcedureVideo)
            VALUES (%s, %s, %s)
        """, (
            read_binary_file(r'medicaldata\StandardVideo\SurgicalProcedureVideo1.mp4'),
            read_binary_file(r'medicaldata\StandardVideo\NursingStandardVideo1.mp4'),
            read_binary_file(r'D:\JiRuan_Projects\database_for_jiruan\medicaldata\StandardVideo\SurgicalProcedureVideo1.mp4')
        ))

    connection.commit()
    print("数据插入成功！")

except Exception as e:
    print(f"发生错误：{e}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()
