from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    
class studenthistory(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    course=models.CharField(max_length=50)