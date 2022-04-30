from django.db import models


# Create your models here.

class InfoModel(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    phnum = models.IntegerField(max_length=10)
    age = models.IntegerField(max_length=2)
    
    
