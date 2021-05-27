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
            to_do = request.POST.get('to_do')
            yearly_to_do = request.POST.get('yearly_to_do')
            yearly_to_do_emotion = request.POST.get('yearly_emotion')
            yearly_to_do_rating = int(request.POST.get('slide1')) + 1
            monthly_to_do = request.POST.get('monthly_to_do')
            monthly_to_do_emotion = request.POST.get('monthly_emotion') 
            monthly_to_do_rating = int(request.POST.get('slide2')) + 1
            weekly_to_do = request.POST.get('weekly_to_do')
            weekly_to_do_emotion = request.POST.get('weekly_emotion')
            weekly_to_do_rating = int(request.POST.get('slide3')) + 1
            daily_to_do = request.POST.get('daily_to_do')
            daily_to_do_emotion = request.POST.get('daily_emotion')
            daily_to_do_rating = int(request.POST.get('slide4')) + 1
            new_to_do = To_Do()
            new_to_do.user = current_user
            new_to_do.age = age
            new_to_do.gender = gender
            new_to_do.to_do = to_do
            new_to_do.yearly_to_do = yearly_to_do
            new_to_do.yearly_to_do_emotion = yearly_to_do_emotion
            new_to_do.yearly_to_do_rating = yearly_to_do_rating
            new_to_do.monthly_to_do = monthly_to_do
            new_to_do.monthly_to_do_emotion = monthly_to_do_emotion
            new_to_do.monthly_to_do_rating = monthly_to_do_rating
            new_to_do.weekly_to_do = weekly_to_do
            new_to_do.weekly_to_do_emotion = weekly_to_do_emotion
            new_to_do.weekly_to_do_rating = weekly_to_do_rating
            new_to_do.daily_to_do = daily_to_do
            new_to_do.daily_to_do_emotion =  daily_to_do_emotion
            new_to_do.daily_to_do_rating = daily_to_do_rating
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
                
                To_do = request.POST.get('to_do')
                yearly_to_do = request.POST.get('yearly_to_do')
                yearly_to_do_emotion = request.POST.get('yearly_emotion')
                yearly_to_do_rating = int(request.POST.get('slide1')) + 1
                monthly_to_do = request.POST.get('monthly_to_do')
                monthly_to_do_emotion = request.POST.get('monthly_emotion') 
                monthly_to_do_rating = int(request.POST.get('slide2')) + 1
                weekly_to_do = request.POST.get('weekly_to_do')
                weekly_to_do_emotion = request.POST.get('weekly_emotion')
                weekly_to_do_rating = int(request.POST.get('slide3')) + 1
                daily_to_do = request.POST.get('daily_to_do')
                daily_to_do_emotion = request.POST.get('daily_emotion')
                daily_to_do_rating = int(request.POST.get('slide4')) + 1
                new_to_do = to_do
                new_to_do.to_do = To_do
                new_to_do.yearly_to_do = yearly_to_do
                new_to_do.yearly_to_do_emotion = yearly_to_do_emotion
                new_to_do.yearly_to_do_rating = yearly_to_do_rating
                new_to_do.monthly_to_do = monthly_to_do
                new_to_do.monthly_to_do_emotion = monthly_to_do_emotion
                new_to_do.monthly_to_do_rating = monthly_to_do_rating
                new_to_do.weekly_to_do = weekly_to_do
                new_to_do.weekly_to_do_emotion = weekly_to_do_emotion
                new_to_do.weekly_to_do_rating = weekly_to_do_rating
                new_to_do.daily_to_do = daily_to_do
                new_to_do.daily_to_do_emotion =  daily_to_do_emotion
                new_to_do.daily_to_do_rating = daily_to_do_rating
                new_to_do.save()
                return redirect('/home')
        else:
                all_emotions = emotions.objects.all()
                temp1 = to_do.yearly_to_do_rating
                temp2 = to_do.monthly_to_do_rating
                temp3 = to_do.weekly_to_do_rating
                temp4 = to_do.daily_to_do_rating
                
                slidearr =[temp1, temp2, temp3, temp4]
                
                to_do.yearly_to_do_rating -= 1
                to_do.monthly_to_do_rating -= 1 
                to_do.weekly_to_do_rating -= 1
                to_do.daily_to_do_rating -= 1
                context = {
                        'to_do':to_do,
                        'all_emotions': all_emotions,
                        'slidearr':slidearr
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
                end_yearly_to_do_emotion = request.POST.get('end_yearly_emotion')
                end_yearly_to_do_rating = int(request.POST.get('slide1')) + 1
                end_monthly_to_do_emotion = request.POST.get('end_monthly_emotion') 
                end_monthly_to_do_rating = int(request.POST.get('slide2')) + 1
                end_weekly_to_do_emotion = request.POST.get('end_weekly_emotion')
                end_weekly_to_do_rating = int(request.POST.get('slide3')) + 1
                end_daily_to_do_emotion = request.POST.get('end_daily_emotion')
                end_daily_to_do_rating = int(request.POST.get('slide4')) + 1
                to_do.end_yearly_to_do_emotion = end_yearly_to_do_emotion
                to_do.end_yearly_to_do_rating = end_yearly_to_do_rating
                to_do.end_monthly_to_do_emotion = end_monthly_to_do_emotion
                to_do.end_monthly_to_do_rating =  end_monthly_to_do_rating
                to_do.end_weekly_to_do_emotion = end_weekly_to_do_emotion
                to_do.end_weekly_to_do_rating =  end_weekly_to_do_rating
                to_do.end_daily_to_do_emotion =  end_daily_to_do_emotion
                to_do.end_daily_to_do_rating = end_daily_to_do_rating
                to_do.is_completed = True
                to_do.save()
                return redirect('/home')
        else:
                if to_do_done==True:
                        to_do.is_completed = False
                        to_do.save()
                        return redirect('/home')
                all_emotions = emotions.objects.all() 
                context = {
                        'to_do': to_do,
                        'all_emotions': all_emotions
                }
                return render(request, 'end_to_do.html', context)

