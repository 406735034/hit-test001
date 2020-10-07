import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *

from django.contrib.auth.models import Group

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


from .forms import RegisterForm, ResetForm

from .decorators import unauthenticated_user, allowed_users, admin_only

from django.views.generic import TemplateView

# Rest Framework
from rest_framework import viewsets

from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserSerializer


class UserCreateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@unauthenticated_user
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password incorrect .... !!!!')
    return render(request, 'login.html')


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, '用戶名或密碼不正確 .... !!!!')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Students')
            user.groups.add(group)
            StudentProfile.objects.create(studentname=user)
            DailyActivity.objects.create(studentname=user)
            Webdata.objects.create(studentname=user)
            messages.success(request, 'Account Created for ' + username)
            return redirect('login')
        else:
            messages.error(request, 'Error')

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='login')
@admin_only
def dashboard(request):

    return render(request, 'home.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'Students'])
def userPage(request):
    profile = StudentProfile.objects.get(studentname_id=request.user.id)
    activity = DailyActivity.objects.get(studentname_id=request.user.id)
    webdata = Webdata.objects.get(studentname_id=request.user.id)
    if activity.today_calories < 100:
        activity.is_today_calories = False
    else:
        activity.is_today_calories = True
    if activity.today_steps < 100:
        activity.is_today_steps = False
    else:
        activity.is_today_steps = True
    if activity.today_sleep < 100:
        activity.is_today_sleep = False
    else:
        activity.is_today_sleep = True
    context = {'profile': profile, 'webdata': webdata, 'activity': activity}
    return render(request, 'user-home.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'Students'])
def userRecPage(request):
    return render(request, 'user-record.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'Students'])
def userAwards(request):
    return render(request, 'user-awards.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'Students'])
def userRanks(request):
    print('users')
    return render(request, 'user-rankings.html')


@login_required(login_url='login')
def restrict(request):
    return render(request, 'restrict.html')
