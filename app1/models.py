from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(models.Model):
    ROLES = (
        ('user', 'User'),
        ('Administrator', 'Administrator'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    role = models.CharField(max_length=30, choices=ROLES,null=True)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.username