from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from PM.forms import UserForm, LoginForm
from .models import User
# Create your views here.
count=0
def main(request):
    return render(request, 'main.html')

def home(request):
    return render(request, 'base.html')

def login(request):
    user=LoginForm(request.GET or None)
    if user.is_valid():
        views.main
    return render(request, 'login.html', {'form':user})
    
def signup(request):
    user = UserForm(request.POST or None)
    if user.is_valid():
        user.save()
        return redirect('http://127.0.0.1:8000/main/')
    return render(request, 'signup.html', {'form':user})