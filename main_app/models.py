from django.db import models
from accounts.models import CustomUser
# Create your models here.

class To_Do(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    age = models.IntegerField(default=0)
    gender = models.TextField(default="None")
    yearly_to_do = models.TextField(max_length=1000)
    monthly_to_do = models.TextField(max_length=1000)
    weekly_to_do = models.TextField(max_length=1000)
    daily_to_do = models.TextField(max_length=1000)
    yearly_to_do_emotion = models.TextField(max_length=1000)
    monthly_to_do_emotion = models.TextField(max_length=1000)
    weekly_to_do_emotion = models.TextField(max_length=1000)
    daily_to_do_emotion = models.TextField(max_length=1000)
    yearly_to_do_rating = models.IntegerField()
    monthly_to_do_rating = models.IntegerField()
    weekly_to_do_rating = models.IntegerField()
    daily_to_do_rating = models.IntegerField()

    end_yearly_to_do_rating = models.IntegerField()
    end_monthly_to_do_rating = models.IntegerField()
    end_weekly_to_do_rating = models.IntegerField()
    end_daily_to_do_rating = models.IntegerField()

    is_completed = models.BooleanField(default=False)
    
   

    
                                                                           
                                                                           
                                                                           