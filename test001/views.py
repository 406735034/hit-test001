import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Bandsdata
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import RegisterForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'index.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect ('dashboard')
            else:
                messages.info(request, 'Username or Password incorrect .... !!!!')
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account Created for ' + user)
            else:
                messages.error(request, 'Error')
            
           
        context = {'form': form}
        return render(request, 'register.html', context)

@login_required(login_url='login')
def dashboard(request):
    data = Bandsdata.objects.all()
    return render(request, 'home.html', {'datas': data})
