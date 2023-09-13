from django.db import models

from django.db import models
import datetime
from rest_framework.exceptions import ValidationError


class Department(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    birth_date = models.DateField()
    salary = models.IntegerField()
    receipt_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        date = datetime.date.today()
        if date.year - self.birth_date.year < 25:
            raise ValidationError ("Сотрудники должны быть не младше 25 лет!")
        elif self.receipt_date > date.today():
            raise ValidationError ("Не раньше завтрашнего дня")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname
