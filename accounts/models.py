# Create your models here.
from enum import unique
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

class CustomUser(AbstractUser):
    gender = models.TextField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    

    def __str__(self):
        return str(self.email)

