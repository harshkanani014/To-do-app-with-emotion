from django.contrib import messages
from django.shortcuts import render, redirect
from .models import To_Do, emotions
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
        else:
                all_emotions = emotions.objects.all()
                context = {
                        'all_emotions': all_emotions
                }
                return render(request, 'add_to_do.html', context)

@login_required(login_url="/")
def edit_to_do(request, id):
        to_do = To_Do.objects.get(id=id)
        if request.method=="POST":
                yearly_to_do = request.POST.get('yearly_to_do')
                monthly_to_do = request.POST.get('monthly_to_do') 
                weekly_to_do = request.POST.get('weekly_to_do')
                daily_to_do = request.POST.get('daily_to_do')
                to_do.yearly_to_do = yearly_to_do
                to_do.monthly_to_do = monthly_to_do
                to_do.weekly_to_do = weekly_to_do
                to_do.daily_to_do = daily_to_do
                to_do.save()
                return redirect('/home')
        else:
                context = {
                        'to_do':to_do
                }
                return render(request, 'edit_to_do.html', context)

@login_required(login_url="/")
def delete_to_do(request, id):
        to_do = To_Do.objects.get(id=id)
        if to_do.is_completed==False:
                messages.info(request, "Please complete task before deleting")
                return redirect('/home')

        to_do.is_deleted = True
        to_do.save()
        return redirect('/home')

@login_required(login_url="/")
def complete_to_do(request, id):
        to_do = To_Do.objects.get(id=id)
        to_do_done = to_do.is_completed
        if request.method=="POST":
                if to_do.is_completed == False:
                        to_do.is_completed = True
                else:
                        to_do.is_completed = False
                to_do.save()
                return redirect('/home')
        else:
                if to_do_done==True:
                        to_do.is_completed = False
                        to_do.save()
                        return redirect('/home') 
                context = {
                        'to_do': to_do
                }
                return render(request, 'end_to_do.html', context)

