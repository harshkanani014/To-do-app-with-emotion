from django.contrib import admin
from .models import To_Do
from accounts.models import CustomUser
# Register your models here.

class To_DoAdmin(admin.ModelAdmin):
    readonly_fields = ('age', 'gender')
    list_display = ('user', 'yearly_to_do')

admin.site.register(To_Do, To_DoAdmin)