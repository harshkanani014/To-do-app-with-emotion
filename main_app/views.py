from django.shortcuts import render, redirect
from .models import To_Do
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/")
def add_to_do(request):
    if request.method=="POST":
            current_user = request.user
            age = current_user.age
            gender = current_user.gender
            yearly_to_do = request.POST.get('yearly_to_do')
            monthly_to_do = request.POST.get('monthly_to_do')
            weekly_to_do = request.POST.get('weekly_to_do')
            daily_to_do = request.POST.get('daily_to_do')
            new_to_do = To_Do()
            new_to_do.user = current_user
            new_to_do.age = age
            new_to_do.gender = gender
            new_to_do.yearly_to_do = yearly_to_do
            new_to_do.monthly_to_do = monthly_to_do
            new_to_do.weekly_to_do = weekly_to_do
            new_to_do.daily_to_do = daily_to_do
            new_to_do.save()
            return redirect('/home')
    return redirect('/home')