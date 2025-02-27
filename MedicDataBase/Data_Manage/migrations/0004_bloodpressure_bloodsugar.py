# Generated by Django 5.0.6 on 2024-12-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_manage", "0003_temperature"),
    ]

    operations = [
        migrations.CreateModel(
            name="BloodPressure",
            fields=[
                (
                    "dataid",
                    models.AutoField(
                        db_column="DataID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "imagetype",
                    models.CharField(
                        blank=True, db_column="ImageType", max_length=50, null=True
                    ),
                ),
                (
                    "imagepath",
                    models.CharField(
                        blank=True, db_column="ImagePath", max_length=255, null=True
                    ),
                ),
                (
                    "sourcetype",
                    models.CharField(
                        blank=True, db_column="SourceType", max_length=50, null=True
                    ),
                ),
                (
                    "sourcepath",
                    models.CharField(
                        blank=True, db_column="SourcePath", max_length=255, null=True
                    ),
                ),
                (
                    "sourcefile",
                    models.TextField(blank=True, db_column="SourceFile", null=True),
                ),
                ("image", models.TextField(blank=True, db_column="Image", null=True)),
                (
                    "recorddate",
                    models.DateField(blank=True, db_column="RecordDate", null=True),
                ),
            ],
            options={
                "db_table": "bloodpressure",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="BloodSugar",
            fields=[
                (
                    "dataid",
                    models.AutoField(
                        db_column="DataID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "imagetype",
                    models.CharField(
                        blank=True, db_column="ImageType", max_length=50, null=True
                    ),
                ),
                (
                    "imagepath",
                    models.CharField(
                        blank=True, db_column="ImagePath", max_length=255, null=True
                    ),
                ),
                (
                    "sourcetype",
                    models.CharField(
                        blank=True, db_column="SourceType", max_length=50, null=True
                    ),
                ),
                (
                    "sourcepath",
                    models.CharField(
                        blank=True, db_column="SourcePath", max_length=255, null=True
                    ),
                ),
                (
                    "sourcefile",
                    models.TextField(blank=True, db_column="SourceFile", null=True),
                ),
                ("image", models.TextField(blank=True, db_column="Image", null=True)),
                (
                    "recorddate",
                    models.DateField(blank=True, db_column="RecordDate", null=True),
                ),
            ],
            options={
                "db_table": "bloodsugar",
                "managed": False,
            },
        ),
    ]
