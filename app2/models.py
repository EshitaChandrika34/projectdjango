from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    department = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    roll_number = models.CharField(max_length=20, unique=True)

    address = models.TextField()
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)

    skills = models.CharField(max_length=100)

    learning_mode = models.CharField(max_length=10)

    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    agree_terms = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name
