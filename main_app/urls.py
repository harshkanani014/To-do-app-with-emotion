from django.urls import path, include
from . import views
urlpatterns = [
    path('add_to_do', views.add_to_do, name="AddToDO")
]   