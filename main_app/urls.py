from django.urls import path, include
from . import views
urlpatterns = [
    path('add_to_do', views.add_to_do, name="AddToDO"),
    path('edit_to_do/<id>', views.edit_to_do, name="EditTodo"),
    path('delete_to_do/<id>', views.delete_to_do, name="DeleteTodo"),
    path('complete_to_do/<id>', views.complete_to_do, name="DoneTodo")
]    