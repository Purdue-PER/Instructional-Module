from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.sessions.models import Session

def Energy_Classify(request):
    if even_dist(cnt) == 1:
        return redirect('Energy_HLG/')
    else:
        return redirect('Energy_LLG')

def Forces_Classify(request):
        return redirect('Force_HLG/')


def SHO_Classify(request):
    if even_dist(cnt) == 1:
        return redirect('SHO_HLG/')
    else:
        return redirect('SHO_LLG/')

def Main(request):
    return render(request,'Modules/main.html')

def landing(request):
    return redirect('Auth/login/')