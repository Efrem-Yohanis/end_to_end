from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL after successful login
        else:
            # Handle invalid credentials error
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    all_user=CustomUser.objects.all()
    context={'all_user':all_user}
    return render(request,'Home.html',context)

def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        address = request.POST['address']
        role = request.POST['role']
        date_of_birth = request.POST['date_of_birth']
        if password1 == password2:
            user=User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            if user:
                user.set_password(password1) 
                user.save()
                newuser= CustomUser.objects.create(email=email,first_name=first_name,date_of_birth=date_of_birth,role=role,address=address,phone=phone,password=password1,username=username,last_name=last_name)
                if newuser:
                    messages.success(request,'user successfull created please login using username and password')
                    return redirect('login')
        else:
            messages.error(request,'password not match')
    return render(request,'Registration.html',{})

def update(request,user_id):
    user=CustomUser.objects.get(id=user_id)
    context={'user':user}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        phone = request.POST['phone']
        address = request.POST['address']
        role = request.POST['role']
        date_of_birth = request.POST['date_of_birth']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.phone = phone
        user.address = address
        user.role = role
        user.date_of_birth = date_of_birth
        user.save()
    return render(request,'update.html',context)

def view_detail(request,user_id):
    user=CustomUser.objects.get(id=user_id)
    context={'user':user}
    return render(request,'view_detail.html',context)

def delete(request,user_id):
    user=CustomUser.objects.get(id=user_id)
    user.delete()
    return render(request,'Home.html',{})