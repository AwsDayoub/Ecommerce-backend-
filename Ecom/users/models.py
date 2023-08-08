from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    STATUS = (
        ('manager' , 'manager'),
        ('customer' , 'customer')
    )
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=100,choices=STATUS,default='customer')
    address = models.CharField(max_length=250,default='Syria / Latakia')
    pho = models.CharField(max_length=30,default='xxx')
    
