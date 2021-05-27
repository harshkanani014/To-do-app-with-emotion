# Create your models here.
from enum import unique
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.TextField(max_length=50, default="a")
    gender = models.TextField(max_length=50, default="None")
    age = models.IntegerField(default="0")
    email = models.EmailField(unique=True, default="harsh@gmail.com")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    

    def __str__(self):
        return str(self.email)


class ContactUs(models.Model):
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    subject = models.TextField(max_length=300)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.message)