from django.contrib import admin
from .models import To_Do, emotions
from accounts.models import CustomUser
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
# class todoadmin(admin.ModelAdmin):
#     list_display = ("user", "age", "gender", "to_do", "is_completed", "is_deleted")

class ParticipantResource(resources.ModelResource):
    class Meta:
        model = To_Do
        import_id_fields = ('user', 'age', 'gender', 'to_do','yearly_to_do','yearly_to_do_emotion','yearly_to_do_rating','end_yearly_to_do_emotion','end_yearly_to_do_rating', 'monthly_to_do','monthly_to_do_emotion','monthly_to_do_rating','end_monthly_to_do_emotion','end_monthly_to_do_rating', 'weekly_to_do','weekly_to_do_emotion','weekly_to_do_rating','end_weekly_to_do_emotion','end_weekly_to_do_rating', 'daily_to_do','daily_to_do_emotion','daily_to_do_rating','end_daily_to_do_emotion','end_daily_to_do_rating', 'is_completed', 'is_deleted')
        fields = ('user', 'age', 'gender', 'to_do','yearly_to_do','yearly_to_do_emotion','yearly_to_do_rating','end_yearly_to_do_emotion','end_yearly_to_do_rating', 'monthly_to_do','monthly_to_do_emotion','monthly_to_do_rating','end_monthly_to_do_emotion','end_monthly_to_do_rating', 'weekly_to_do','weekly_to_do_emotion','weekly_to_do_rating','end_weekly_to_do_emotion','end_weekly_to_do_rating', 'daily_to_do','daily_to_do_emotion','daily_to_do_rating','end_daily_to_do_emotion','end_daily_to_do_rating', 'is_completed', 'is_deleted')
        export_order = ('user', 'age', 'gender', 'to_do','yearly_to_do','yearly_to_do_emotion','yearly_to_do_rating','end_yearly_to_do_emotion','end_yearly_to_do_rating', 'monthly_to_do','monthly_to_do_emotion','monthly_to_do_rating','end_monthly_to_do_emotion','end_monthly_to_do_rating', 'weekly_to_do','weekly_to_do_emotion','weekly_to_do_rating','end_weekly_to_do_emotion','end_weekly_to_do_rating', 'daily_to_do','daily_to_do_emotion','daily_to_do_rating','end_daily_to_do_emotion','end_daily_to_do_rating', 'is_completed', 'is_deleted')


class ParticipantDataAdmin(ImportExportActionModelAdmin):
    resource_class = ParticipantResource
    list_display = ('id', 'user', 'age', 'gender', "to_do", 'is_completed', 'is_deleted')


admin.site.register(emotions)
admin.site.register(To_Do, ParticipantDataAdmin)