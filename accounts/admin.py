from django.contrib import admin
from .models import ContactUs, CustomUser
# Register your models here.

admin.site.register(CustomUser)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

admin.site.register(ContactUs, ContactUsAdmin)
