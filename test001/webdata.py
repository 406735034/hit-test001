from time import sleep
import requests
import json
import time
import datetime
from django.utils.timezone import utc

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *

from django.contrib.auth.models import Group, User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


from .forms import RegisterForm, StudentForm

from .decorators import unauthenticated_user, allowed_users, admin_only

from django.views.generic import TemplateView

from django.contrib.auth.models import User


def createuser(request, username, password, role, name):
    u = User.objects.create(
        username=username,
        first_name=name,
    )
    u.set_password(password)
    u.save()
    user = User.objects.get(username=username)
    group = Group.objects.get(name='Students')
    if(role == 16):
        group = Group.objects.get(name='Teachers')
    user.groups.add(group)
    messages.success(request, " ")
    return user


def newpassword(request, username, password):
    try:
        u = User.objects.get(username=username)
        u.set_password(password)
        u.save()
        messages.success(request, " ")

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")

    except Exception as e:
        messages.error(request, "Other Error")

    return None


def wibio_getUser(userId):
    url = "https://health.weiecampus.com/wiBioGolife/user/getUser"

    r = requests.post(url, data={'userid': userId})
    res = r.json()
    if (res['status'] == 1):
        content = json.loads(json.dumps(res['content']))
        profile = json.loads(json.dumps(content['profile']))
        extras = json.loads(json.dumps(profile['characteristic']))
        data = {'profile': profile, 'extras': extras, 'status': res['status']}

    else:
        data = res
    return data


def wibio_getuserIdActivity(userId, date):
    url = "https://health.weiecampus.com/wiBioGolife/statistic/school/getDailyHealth"

    r = requests.post(url, data={'schoolid': '4576', 'date': date})
    res = r.json()
    data = {}
    if (res['status'] == 1):
        content = json.loads(json.dumps(res['content']))

        for i in content:
            act1 = i['userId']
            if(act1 == userId):
                data = i

        print(data)

    return data


# def wibio_getActivity():
#     url = "https://health.weiecampus.com/wiBioGolife/statistic/getDailyActivity"

#     r = requests.post(
#         url, data={'userid': '4582', 'date': '1605306986000'})
#     res = r.json()
#     return res


@ login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        epdate = request.POST['epdate']
        date = request.POST['date']
        print(epdate, date)
        a = StudentProfile.objects.get(studentname=request.user)
        userId = a.userId
        print(userId)
        # wibio_getuserIdActivity( userId, epdate)
        wibio_getAllActivity(request, epdate)
        # wibio_getUpdateActivity( epdate, date)
    return render(request, 'update.html')


def wibio_getUpdateActivity(epdate, date):
    url = "https://health.weiecampus.com/wiBioGolife/statistic/school/getDailyHealth"

    r = requests.post(url, data={'schoolid': '4576', 'date': epdate})
    res = r.json()
    data = {}

    if (res['status'] == 1):
        content = json.loads(json.dumps(res['content']))
        for i in content:
            userId = i['userId']
            username = i['account']
            userInfo = wibio_getUser(userId)
            name = userInfo['profile']['name']
            role = userInfo['profile']['roleType']
            totalSteps = i['activity']['totalSteps']
            totalCalories = i['activity']['totalCalories']
            stepsGoal = i['activity']['stepsGoal']
            caloriesGoal = i['activity']['caloriesGoal']
            sleepscore = i['sleep']['score']*100
            heartmax = i['heart']['max']
            heartmin = i['heart']['min']
            hearttotal = i['heart']['total']

    return data


def wibio_getAllActivity(request, epdate):
    url = "https://health.weiecampus.com/wiBioGolife/statistic/school/getDailyHealth"

    r = requests.post(url, data={'schoolid': '4576', 'date': epdate})
    res = r.json()
    data = {}
    userIdList = []
    if (res['status'] == 1):
        content = json.loads(json.dumps(res['content']))
        for i in content:
            act1 = i['account']
            userIdList.append(act1)

            userId = i['userId']
            username = i['account']
            userInfo = wibio_getUser(userId)
            name = userInfo['profile']['name']
            role = userInfo['profile']['roleType']
            password = 'edu@3231'
            try:
                u = User.objects.get(username=username)
                a = DailyActivity.objects.get(user_id=u.id)

            except User.DoesNotExist:
                messages.error(request, "Other Error")
                # user = createuser(request, username, password, role, name)

            except Exception as e:
                messages.error(request, "Other Error")

    return data
