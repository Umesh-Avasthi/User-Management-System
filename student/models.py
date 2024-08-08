from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=20,null=False)
    email=models.EmailField(max_length=20,null=False)
    phone=models.CharField(max_length=10,null=False)
    city=models.CharField(max_length=10,null=False)
    course=models.CharField(max_length=15,null=False)
    
class studenthistory(models.Model):
    name=models.CharField(max_length=20,null=False)
    email=models.EmailField(max_length=20,null=False)
    phone=models.CharField(max_length=10,null=False)
    city=models.CharField(max_length=10,null=False)
    course=models.CharField(max_length=15,null=False)