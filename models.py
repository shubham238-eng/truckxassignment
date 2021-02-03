from django.db import models


# Create your models here.
class Alarm_type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)


class AlarmTable(models.Model):  # have to add non null constrain
    Imei = models.CharField(max_length=100, unique=True)
    id = models.AutoField(primary_key=True)
    alarm_type = models.ForeignKey(Alarm_type, on_delete=models.CASCADE)
    alarm_time = models.DateTimeField()
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)


class file_list(models.Model):
    file_name = models.CharField(max_length=100)
    ids = models.ForeignKey(AlarmTable, on_delete=models.CASCADE)


class VideoUpload(models.Model):
    imei = models.CharField(max_length=10)
    file_list = models.FileField(upload_to='media/% Y/% m/% d/')
