from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Homepage, name="HomePage"),
    path('register', views.Register, name="Register"),
    path('signin', views.signin, name="signin"),
    path('home', views.To_Do_page, name="ToDO"),
    path('signout', views.signout, name="Signout")
]
