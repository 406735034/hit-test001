from time import process_time, sleep
import requests
import json
from datetime import date, timedelta
import time
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

# Rest Framework
from rest_framework import viewsets

from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
timenow = int(time.time()*1000)
today = date.today()
yesterday = today - timedelta(1)


class ChartWeekData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        week_categories = [
            "Mon",
            "星期二",
            "星期三",
            "星期四",
            "星期五",
            "星期六",
            "星期日",
        ]
        data = 3700
        # {'catgs': week_categories}

        return Response(data)


# userId = 4575


class UserCreateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


def wibio_login(account, password):

    url = "https://health.weiecampus.com/wiBioGolife/oauth/login"
    r = requests.post(
        url, data={'account': account, 'password': password})
    res = r.json()
    if (res['status'] == 1):
        content = json.loads(json.dumps(res['content']))
        schoollist = content['schoolList'][0]
        schoollist = json.loads(json.dumps(schoollist))
        data = {'content': content, 'school': schoollist,
                'status': res['status']}

    else:
        data = res
    return data


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

    return data


def wibio_getActivity():
    url = "https://health.weiecampus.com/wiBioGolife/statistic/getDailyActivity"

    r = requests.post(
        url, data={'userid': '4582', 'date': '1605306986000'})
    res = r.json()
    return res


def update(request):

    dformat_str = '%Y-%m-%d'
    if request.method == 'POST':
        start_date_str = request.POST.get("startdate")
        end_date_str = request.POST.get("enddate")
        if(start_date_str <= end_date_str):
            if(end_date_str <= str(today)):
                start_date = datetime.datetime.strptime(
                    start_date_str, dformat_str)
                end_date = datetime.datetime.strptime(
                    end_date_str, dformat_str)

                for single_date in daterange(start_date, end_date+timedelta(1)):
                    epdate = int(single_date.timestamp())*1000
                    wibio_getAllActivity(request, single_date, epdate)

                wibio_getAllActivity(request, today, timenow)
                messages.success(request, "更新完成..!")
            else:
                messages.error(request, "結束日不能大於今日..!")

        else:
            messages.error(request, "啟始日不能大於結束日..!")

    return render(request, 'update.html')


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def wibio_getAllActivity(request, date, epdate):
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
            steps = i['activity']['totalSteps']
            calories = i['activity']['totalCalories']
            stepsgoal = i['activity']['stepsGoal']
            caloriesgoal = i['activity']['caloriesGoal']
            sleepscore = i['sleep']['score']*100
            heartmax = i['heart']['max']
            heartmin = i['heart']['min']
            hearttotal = i['heart']['total']

            try:
                User.objects.get(username=username)

            except User.DoesNotExist:
                password = 'edu@3231'
                createuser(request, username, password, role, name)

            except Exception as e:
                messages.error(request, "Other User Creation Error")

            u = User.objects.get(username=username)
            try:
                a = DailyActivity.objects.get(
                    act_date=date, user_id=u.id)
                a.steps = steps
                a.stepsgoal = stepsgoal
                a.calories = calories
                a.caloriesgoal = caloriesgoal
                a.sleepscore = sleepscore
                a.heartmax = heartmax
                a.heartmin = heartmin
                a.hearttotal = hearttotal
                a.save()

            except DailyActivity.DoesNotExist:
                DailyActivity.objects.create(act_date=date, user_id=u.id)
                a = DailyActivity.objects.get(
                    act_date=date, user_id=u.id)
                a.steps = steps
                a.stepsgoal = stepsgoal
                a.calories = calories
                a.caloriesgoal = caloriesgoal
                a.sleepscore = sleepscore
                a.heartmax = heartmax
                a.heartmin = heartmin
                a.hearttotal = hearttotal
                a.save()
            except Exception as e:
                messages.error(request, "Other Activity Error")
                print('error')

    return False


@unauthenticated_user
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Teachers'])
def teacherPage(request):
    users = User.objects.all()
    profile = StudentProfile.objects.get(studentname_id=request.user.id)
    context = {'users': users, 'profile': profile}
    return render(request, 'teacher-home.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        res = wibio_login(username, password)
        status = res['status']
        if(username == 'Admin'):
            status = 1

        if (status == 1):
            role = res['school']['role']
            userId = res['content']['userId']
            userInfo = wibio_getUser(userId)
            name = userInfo['profile']['name']
            weight = userInfo['extras']['weight']
            height = userInfo['extras']['height']

            try:
                User.objects.get(username=username)
                newpassword(request, username, password)
            except User.DoesNotExist:
                createuser(request, username, password, role, name)

            except Exception as e:
                messages.error(request, "Error in getting user/creating user!")

            user = authenticate(
                request, username=username, password=password)

            # try:
            #     StudentProfile.objects.get(studentname=user)
            # except StudentProfile.DoesNotExist:
            #     StudentProfile.objects.create(studentname=user)
            # except Exception as e:
            #     messages.error(
            #         request, "Error in getting/creating user profile!")

            try:
                DailyActivity.objects.get(act_date=today, user_id=user.id)
                i = wibio_getuserIdActivity(userId, timenow)
                a = DailyActivity.objects.get(act_date=today, user_id=user.id)
                a.steps = i['activity']['totalSteps']
                a.stepsgoal = i['activity']['stepsGoal']
                a.calories = i['activity']['totalCalories']
                a.caloriesgoal = i['activity']['caloriesGoal']
                a.sleepscore = i['sleep']['score']*100
                a.heartmax = i['heart']['max']
                a.heartmin = i['heart']['min']
                a.hearttotal = i['heart']['total']
                a.save()

            except DailyActivity.DoesNotExist:
                i = wibio_getuserIdActivity(userId, timenow)
                DailyActivity.objects.create(act_date=today, user_id=user.id)
                a = DailyActivity.objects.get(act_date=today, user_id=user.id)
                a.steps = i['activity']['totalSteps']
                a.stepsgoal = i['activity']['stepsGoal']
                a.calories = i['activity']['totalCalories']
                a.caloriesgoal = i['activity']['caloriesGoal']
                a.sleepscore = i['sleep']['score']*100
                a.heartmax = i['heart']['max']
                a.heartmin = i['heart']['min']
                a.hearttotal = i['heart']['total']
                a.save()
            except Exception as e:
                messages.error(
                    request, "probably today activity already exists!")
            try:
                DailyActivity.objects.get(
                    act_date=yesterday, user_id=user.id)
            except DailyActivity.DoesNotExist:
                i = wibio_getuserIdActivity(userId, yesterday)

                a = DailyActivity.objects.create(
                    act_date=yesterday, user_id=user.id)
                a.steps = i['activity']['totalSteps']
                a.stepsgoal = i['activity']['stepsGoal']
                a.calories = i['activity']['totalCalories']
                a.caloriesgoal = i['activity']['caloriesGoal']
                a.sleepscore = i['sleep']['score']*100
                a.heartmax = i['heart']['max']
                a.heartmin = i['heart']['min']
                a.hearttotal = i['heart']['total']
                a.save()

            u = StudentProfile.objects.get(studentname=user)
            u.SchoolId = res['school']['id']
            if(res['school']['name'] == '高雄市立大同國民小學'):
                u.School = '大同國小'
            else:
                u.School = res['school']['name']
            u.gender = userInfo['profile']['gender']
            u.userId = userId
            u.birthday = userInfo['extras']['birthday']
            u.weight = weight
            u.height = height
            u.BMI = round(weight / ((height/100)*(height/100)), 2)
            u.save()

            if user is not None:
                login(request, user)
                group = str(Group.objects.get(user=user))
                if group == "Admins":
                    return redirect('dashboard')
                elif group == 'Teachers':
                    print('teacher login!')
                    return redirect('teacher-page')
                elif group == 'Students':
                    return redirect('user-page')

        else:
            messages.info(request, '用戶名或密碼不正確 .... !!!!')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['Admins'])
def dashboard(request):
    students = StudentProfile.objects.all()
    context = {'students': students, }
    return render(request, 'dashboard.html', context)


def ranking(day1, qs):
    stepranks = DailyActivity.objects.filter(act_date=day1).order_by('-steps')
    slpranks = DailyActivity.objects.filter(
        act_date=day1).order_by('-sleepscore')
    cal_ranks = DailyActivity.objects.filter(
        act_date=day1).order_by('-calories')
    stp = getrank(stepranks, qs)
    slp = getrank(slpranks, qs)
    cal = getrank(cal_ranks, qs)
    mystprnk = stp
    myslprnk = slp
    mycalrnk = cal
    steprank1 = stepranks[0].user.studentname.first_name
    try:
        steprank2 = stepranks[1].user.studentname.first_name
    except:
        steprank2 = "N/A"
    try:
        steprank3 = stepranks[2].user.studentname.first_name
    except:
        steprank3 = "N/A"
    slprank1 = slpranks[0].user.studentname.first_name
    try:
        slprank2 = slpranks[1].user.studentname.first_name
    except:
        slprank2 = "N/A"
    try:
        slprank3 = slpranks[2].user.studentname.first_name
    except:
        slprank3 = "N/A"
    calrank1 = cal_ranks[0].user.studentname.first_name
    try:
        calrank2 = cal_ranks[1].user.studentname.first_name
    except:
        calrank2 = "N/A"
    try:
        calrank3 = cal_ranks[2].user.studentname.first_name
    except:
        calrank3 = "N/A"
    context = {'steprank1': steprank1,
               'steprank2': steprank2, 'steprank3': steprank3,
               'mystprank': mystprnk,
               'slprank1': slprank1,
               'slprank2': slprank2, 'slprank3': slprank3,
               'myslprank': myslprnk,
               'calrank1': calrank1,
               'calrank2': calrank2, 'calrank3': calrank3,
               'mycalrank': mycalrnk, }
    return context


def getrank(qs, ms):

    j = 0
    k = 0
    for i in qs:
        if (i == ms):
            k = j
        j += 1
    return k+1


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['Students'])
def userPage(request):
    todayActivity = DailyActivity.objects.get(
        act_date=today, user_id=request.user.id)
    yesterdayActivity = DailyActivity.objects.get(
        act_date=yesterday, user_id=request.user.id)
    profile = StudentProfile.objects.get(studentname_id=request.user.id)

    qsd = []
    qsme = DailyActivity.objects.filter(user_id=request.user.id)
    for i in qsme:
        qsd.append(i.steps)

    todayrank = ranking(today, todayActivity)
    if(yesterdayActivity.stepsgoal <= 0):
        yesterdayActivity.stepsgoal = 1
    if(yesterdayActivity.caloriesgoal <= 0):
        yesterdayActivity.caloriesgoal = 1
    yd_step = round((yesterdayActivity.steps /
                     yesterdayActivity.stepsgoal)*100, 2)
    yd_cal = round((yesterdayActivity.calories /
                    yesterdayActivity.caloriesgoal)*100, 2)
    yd_sleep = yesterdayActivity.sleepscore
    if(todayActivity.stepsgoal <= 0):
        todayActivity.stepsgoal = 1
    if(todayActivity.caloriesgoal <= 0):
        todayActivity.caloriesgoal = 1
    td_step = round((todayActivity.steps /
                     todayActivity.stepsgoal)*100, 2)
    td_cal = round((todayActivity.calories /
                    todayActivity.caloriesgoal)*100, 2)
    td_sleep = todayActivity.sleepscore

    webdata = Webdata.objects.get(studentname_id=request.user.id)
    if (webdata.lesson1finish == 0):
        less1finish = 100
        less1coment = "開始閱讀!"
    else:
        less1finish = webdata.lesson1finish
        less1coment = str(webdata.lesson1finish) + '%'
    if (webdata.lesson2finish == 0):
        less2finish = 100
        less2coment = "開始閱讀!"
    else:
        less2finish = webdata.lesson2finish
        less2coment = str(webdata.lesson2finish) + '%'
    if (webdata.lesson3finish == 0):
        less3finish = 100
        less3coment = "開始閱讀!"
    else:
        less3finish = webdata.lesson3finish
        less3coment = str(webdata.lesson3finish) + '%'

    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Error')
    # if (profile.gender == 2):
    #     if (profile.BMI < 18.5):
    #         BMIC = "體重不足"
    #     elif (profile.BMI >= 18.5 & profile.BMI <= 24.9):
    #         BMIC = "健康"
    #     else:
    #         BMIC = "超重"

    # else:
    #     if (profile.BMI < 18.5):
    #         BMIC = "體重不足"
    #     elif (profile.BMI >= 18.5 & profile.BMI <= 24.9):
    #         BMIC = "健康"
    #     else:
    #         BMIC = "超重"

    context = {'profile': profile, 'webdata': webdata,
               'form': form, 'less1data': less1finish,
               'less1cmnt': less1coment, 'less2data': less2finish,
               'less2cmnt': less2coment, 'less3data': less3finish,
               'less3cmnt': less3coment, 'yd_step': yd_step, 'yd_cal': yd_cal, 'yd_sleep': yd_sleep,
               'td_step': td_step, 'td_cal': td_cal, 'td_sleep': td_sleep, 'todayrank': todayrank,
               }
    return render(request, 'user-home.html', context)


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['admins', 'Students'])
def userRecPage(request):
    return render(request, 'user-record.html')


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['admins', 'Students'])
def userAwards(request):
    return render(request, 'user-awards.html')


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['admins', 'Students'])
def userRanks(request):

    return render(request, 'user-rankings.html')


@ login_required(login_url='login')
def restrict(request):
    group = str(Group.objects.filter(user=request.user)[0])
    if group == "Admins":
        return redirect('dashboard')
    elif group == 'Teacher':
        return redirect('teacher-page')
    elif group == 'Students':
        return redirect('user-page')
    else:
        return render(request, 'restrict.html')


@ login_required(login_url='login')
def lesson1(request):
    return render(request, 'lesson1.html')


@ login_required(login_url='login')
def lesson2(request):
    return render(request, 'lesson2.html')


@ login_required(login_url='login')
def lesson3(request):
    return render(request, 'lesson3.html')


@ login_required(login_url='login')
def game(request):
    return render(request, 'gamewindow.html')
