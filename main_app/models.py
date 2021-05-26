from django.db import models
from accounts.models import CustomUser
# Create your models here.

class emotions(models.Model):
    emotion = models.TextField(max_length=50)

class To_Do(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    age = models.IntegerField(default=0, blank=True)
    gender = models.TextField(default="None", blank=True)
    to_do = models.TextField(max_length=1000, default="Add todo")
    yearly_to_do = models.TextField(max_length=1000, blank=True)
    monthly_to_do = models.TextField(max_length=1000,  blank=True)
    weekly_to_do = models.TextField(max_length=1000,  blank=True)
    daily_to_do = models.TextField(max_length=1000,  blank=True)
    yearly_to_do_emotion = models.TextField(max_length=1000,  blank=True)
    monthly_to_do_emotion = models.TextField(max_length=1000,  blank=True)
    weekly_to_do_emotion = models.TextField(max_length=1000,  blank=True)
    daily_to_do_emotion = models.TextField(max_length=1000,  blank=True)
    yearly_to_do_rating = models.IntegerField(blank=True, default=-1)
    monthly_to_do_rating = models.IntegerField(blank=True, default=-1)
    weekly_to_do_rating = models.IntegerField(blank=True, default=-1)
    daily_to_do_rating = models.IntegerField(blank=True, default=-1)

    end_yearly_to_do_rating = models.IntegerField(blank=True, default=-1)
    end_monthly_to_do_rating = models.IntegerField(blank=True, default=-1)
    end_weekly_to_do_rating = models.IntegerField(blank=True, default=-1)
    end_daily_to_do_rating = models.IntegerField(blank=True, default=-1)

    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
   

    
                                                                           
                                                                           
                                                                           