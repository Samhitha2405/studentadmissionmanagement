from django.db import models

# Create your models here.
# models.py

from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField(default='1900-01-01')  # Assuming a default date of birth
    aadhar_number = models.CharField(max_length=12, default='')
    memo = models.FileField(upload_to='static/studentfiles/')
    photo = models.ImageField(upload_to='static/images/students/')
    email = models.EmailField(default='')
    mother_name = models.CharField(max_length=100, default='Unknown')
    father_name = models.CharField(max_length=100, default='')
    student_phone_number = models.CharField(max_length=15, default='')
    parent_phone_number = models.CharField(max_length=15, default='')
    assign_id_number = models.CharField(max_length=20, default='N/A')

    class Meta:
        db_table="Student"


