import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import banddata
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import RegisterForm, ResetForm

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
@unauthenticated_user
def home(request):
    return render(request, 'index.html')

@unauthenticated_user
def loginPage(request):

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

@unauthenticated_user
def register(request):

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Students')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request,'Account Created for ' + username)
        else:
            messages.error(request, 'Error')
        
        
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='login')
@admin_only
def dashboard(request):
    data = banddata.objects.filter(male='Yes')
    return render(request, 'home.html', {'datas': data})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins','Students'])
def userPage(request):
    context = {}
    return render(request, 'user.html', context)

@login_required(login_url='login')
def restrict(request):
    
    return render(request,'restrict.html')
