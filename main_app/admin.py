from django.contrib import admin
from .models import To_Do, emotions
from accounts.models import CustomUser
# Register your models here.


admin.site.register(emotions)
admin.site.register(To_Do)