# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Audiorecord(models.Model):
    recordid = models.AutoField(db_column='RecordID', primary_key=True)  # Field name made lowercase.
    counselingaudio = models.TextField(db_column='CounselingAudio', blank=True, null=True)  # Field name made lowercase.
    postopcareaudio = models.TextField(db_column='PostOpCareAudio', blank=True, null=True)  # Field name made lowercase.
    conditionchangeaudio = models.TextField(db_column='ConditionChangeAudio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'audiorecord'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bloodpressure(models.Model):
    dataid = models.AutoField(db_column='DataID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourcepath = models.CharField(db_column='SourcePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcefile = models.TextField(db_column='SourceFile', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    recorddate = models.DateField(db_column='RecordDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bloodpressure'


class Bloodsugar(models.Model):
    dataid = models.AutoField(db_column='DataID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourcepath = models.CharField(db_column='SourcePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcefile = models.TextField(db_column='SourceFile', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    recorddate = models.DateField(db_column='RecordDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bloodsugar'


class Department(models.Model):
    departmentid = models.AutoField(db_column='DepartmentID', primary_key=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=255)  # Field name made lowercase.
    hospitalid = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='HospitalID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class Devicedata(models.Model):
    dataid = models.AutoField(db_column='DataID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datacontent = models.TextField(db_column='DataContent', blank=True, null=True)  # Field name made lowercase.
    recorddate = models.DateField(db_column='RecordDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'devicedata'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctor(models.Model):
    doctorid = models.AutoField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    specialty = models.CharField(db_column='Specialty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactinfo = models.CharField(db_column='ContactInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctor'


class Document(models.Model):
    documentid = models.AutoField(db_column='DocumentID', primary_key=True)  # Field name made lowercase.
    admissionrecord = models.TextField(db_column='AdmissionRecord', blank=True, null=True)  # Field name made lowercase.
    dischargesummary = models.TextField(db_column='DischargeSummary', blank=True, null=True)  # Field name made lowercase.
    treatmentplan = models.TextField(db_column='TreatmentPlan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'document'


class Genomicdata(models.Model):
    geneid = models.AutoField(db_column='GeneID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    genesequence = models.TextField(db_column='GeneSequence', blank=True, null=True)  # Field name made lowercase.
    analysisresult = models.TextField(db_column='AnalysisResult', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genomicdata'


class Hospital(models.Model):
    hospitalid = models.AutoField(db_column='HospitalID', primary_key=True)  # Field name made lowercase.
    hospitalname = models.CharField(db_column='HospitalName', max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactinfo = models.CharField(db_column='ContactInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hospital'


class Medicalimage(models.Model):
    imageid = models.AutoField(db_column='ImageID', primary_key=True)  # Field name made lowercase.
    recordid = models.ForeignKey('Medicalrecord', models.DO_NOTHING, db_column='RecordID', blank=True, null=True)  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    storagepath = models.CharField(db_column='StoragePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uploaddate = models.DateField(db_column='UploadDate', blank=True, null=True)  # Field name made lowercase.
    ctimage = models.TextField(db_column='CTImage', blank=True, null=True)  # Field name made lowercase.
    mriimage = models.TextField(db_column='MRIImage', blank=True, null=True)  # Field name made lowercase.
    ultrasoundimage = models.TextField(db_column='UltrasoundImage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicalimage'


class Medicalrecord(models.Model):
    recordid = models.AutoField(db_column='RecordID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    doctorid = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    diagnosisdate = models.DateField(db_column='DiagnosisDate')  # Field name made lowercase.
    diagnosisresult = models.TextField(db_column='DiagnosisResult', blank=True, null=True)  # Field name made lowercase.
    prescription = models.TextField(db_column='Prescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicalrecord'


class Patient(models.Model):
    patientid = models.AutoField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
    contactinfo = models.CharField(db_column='ContactInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'


class Standardvideo(models.Model):
    videoid = models.AutoField(db_column='VideoID', primary_key=True)  # Field name made lowercase.
    surgicalprocedurevideo = models.TextField(db_column='SurgicalProcedureVideo', blank=True, null=True)  # Field name made lowercase.
    nursingstandardvideo = models.TextField(db_column='NursingStandardVideo', blank=True, null=True)  # Field name made lowercase.
    emergencyprocedurevideo = models.TextField(db_column='EmergencyProcedureVideo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'standardvideo'


class Temperature(models.Model):
    dataid = models.AutoField(db_column='DataID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourcepath = models.CharField(db_column='SourcePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcefile = models.TextField(db_column='SourceFile', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    recorddate = models.DateField(db_column='RecordDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temperature'
