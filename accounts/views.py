from django.shortcuts import redirect, render
from .models import CustomUser
import hashlib
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main_app.models import To_Do
# Create your views here.

def Homepage(request):
    return render(request, "accounts/index.html")

def Register(request):
    if request.method=="POST":
        email = request.POST.get('email')
        try:
            check_user = CustomUser.objects.get(email=email)
            messages.info(request, "User already exists")
            return redirect('/signin')
        except:
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            if password!=confirmpassword:
                messages.warning(request, "Password Does not match")
                return redirect('/register')
            
            password = pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
            print(password)
            #CustomUser.objects.create_user(username=email, )
            new_user = CustomUser()
            new_user.username = email
            new_user.email = email
            new_user.gender = gender
            new_user.age = age
            new_user.password = password
            new_user.save()
            login(request, new_user)
            return redirect('/home')
    else:
        return render(request, "accounts/register.html")

def signin(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_data = CustomUser.objects.get(email=email)
        except:
            messages.warning(request, "Email not found or incorrect")
            return redirect("/signin")
        password_data = user_data.password
        #print(password_data)
        if pbkdf2_sha256.verify(password, password_data):
            #print(password_data)
            login(request, user_data)
            return redirect('/home')
        else:
            messages.warning(request, "Incorrect password")
            return redirect('/signin')
    else:
        return render(request, "accounts/signin.html")

@login_required(login_url="/")
def To_Do_page(request):
    current_user = request.user
    count_incomplete_to_do = To_Do.objects.filter(user=current_user, is_completed=False, is_deleted = False)
    if request.method=="POST":
        search = request.POST.get('search-area') or ''
        if search:
            current_user = request.user
            all_to_dos = To_Do.objects.filter(user=current_user, to_do__startswith=search, is_deleted=False)
            context = {
                'all_to_do': all_to_dos,
                'count': len(count_incomplete_to_do)
            }
            return render(request, "to_do_page.html", context)
        else:
            return redirect('/home')
    else:
        current_user = request.user
        print(current_user)
        all_to_dos = To_Do.objects.filter(user=current_user)
        print(all_to_dos)
        context = {
            'all_to_do': all_to_dos,
            'count': len(count_incomplete_to_do)
        }
        return render(request, 'to_do_page.html', context)

@login_required(login_url="/")
def signout(request):
    logout(request)
    return redirect('/')


