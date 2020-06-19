from django.db import models
from django.utils.timezone import timezone


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class banddata(models.Model):
    username = models.TextField(null=False)
    password = models.TextField(null=False)
    male = models.TextField(null=True)
    female = models.TextField(null=True)
    data_time = models.TextField(null=True)
    userid = models.IntegerField(null=True)
    heart_recordnum = models.IntegerField(null=True)
    heart_max = models.IntegerField(null=True)
    heart_min = models.IntegerField(null=True)
    heart_total = models.IntegerField(null=True)
    sleep_deepsleeptime = models.IntegerField(null=True)
    sleep_lightsleeptime = models.IntegerField(null=True)
    sleep_awaketime = models.IntegerField(null=True)
    sleep_score = models.FloatField(null=True)
    sleep_waketimes = models.IntegerField(null=True)
    activity_totalsteps = models.IntegerField(null=True)
    activity_totalcalories = models.IntegerField(null=True)
    activity_totaldistances = models.IntegerField(null=True)
    activity_moststeps = models.IntegerField(null=True)
    sh150_light = models.IntegerField(null=True)
    sh150_moderate = models.IntegerField(null=True)
    sh150_vigorous = models.IntegerField(null=True)
    hasvalue = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.username


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Reward(models.Model):
    name = models.CharField(max_length=200, null=True)
    points = models.IntegerField(null=True)
    gold = models.IntegerField(null=True)
    gems = models.IntegerField(null=True)
    expire_date = models.DateField(null=True)
    created = models.DateField(auto_now_add=True, null=True)
    font_size = models.IntegerField()

    def __str__(self):
        return self.name


class Workout(models.Model):
    STATUS = (
        ('active', 'active'),
        ('used', 'used'),
        ('expired', 'expired')
    )
    banddata = models.ForeignKey(
        banddata, null=True, on_delete=models.SET_NULL)
    reward = models.ForeignKey(Reward, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS)


class Tamkang(models.Model):
    building = models.TextField(max_length=100, null=True)
    branches = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.building


class userdata(models.Model):
    username = models.CharField(max_length=150, null=True)
    sleep = models.IntegerField()
    walk = models.IntegerField()
    exercise = models.IntegerField()
    calories = models.IntegerField()
    avg_monday = models.IntegerField()
    avg_tuesday = models.IntegerField()
    avg_wednesday = models.IntegerField()
    avg_thursday = models.IntegerField()
    avg_friday = models.IntegerField()
    avg_saturday = models.IntegerField()
    avg_sunday = models.IntegerField()

    def __str__(self):
        return self.username
