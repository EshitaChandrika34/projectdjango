from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Studentdata(models.Model):
    name=models.CharField(max_length=20)

class hello(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    branch=models.CharField(max_length=10,default='IT')


class LoginUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.IntegerField(max_length=10)

    def __str__(self):
        return self.username

from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='colleges/')

