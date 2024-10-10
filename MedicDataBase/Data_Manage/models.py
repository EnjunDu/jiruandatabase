from django.db import models

# Create your models here.

class Data_Manage(models.Model):
    # 受限于数据库暂未确定，因此暂时只有满足运行所需求的字段

    name = models.CharField(max_length=100)
    