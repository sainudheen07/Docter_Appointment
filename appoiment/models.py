from django.db import models
import datetime
from main.models import Docter, Department


class PatientDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.date.today())
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)

    def __str__(self):
        return '{}'.format(self.name)


class Appoiment(models.Model):
    date = models.DateTimeField(default=datetime.date.today())


class Queue(models.Model):
    num = models.IntegerField()
    app_date = models.ForeignKey(Appoiment, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.num)
