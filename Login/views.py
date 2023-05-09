import pandas as pd
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .form import registration_form
from django.contrib import messages 


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username is not correct')
    
        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('/Force/')
        else: 
            messages.error(request,'Password is incorrect')
    
    return render(request,'Login/Login.html')

def logoutUser(request):
    logout(request)
    return render(request,'Login/Logout.html')

def register(request):
    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if email.split(".")[-1] == 'edu':
                print("passed")
                messages.success(request, 'Account created successfully') 
                form.save()
                return redirect("/Auth/login/")
            else:
                print("failed")
                form = registration_form(request.POST)
                messages.error(request, "[Please use school email ending in '@edu']")
                return render(request,'Login/register.html',{"form":form})
        else: 
            errors = form.errors.as_data()
            for key in errors:
                messages.error(request,f"{errors[key][0]}")
            return render(request,'Login/register.html',{"form":form})
            print(form.errors.as_data())
    
    else:
        form = registration_form()
        return render(request,'Login/register.html',{'form':form})