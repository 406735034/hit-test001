from os import name
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.utils.timezone import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    Gender_Choices = [('1', 'Male'), ('2', 'Female')]
    studentname = models.OneToOneField(User, on_delete=models.CASCADE,
                                       primary_key=True,)
    gender = models.CharField(choices=Gender_Choices,
                              max_length=2, default='1')
    photo = models.ImageField(null=True, blank=True,
                              default="naa.png")
    account = models.CharField(max_length=100)
    userId = models.CharField(max_length=255)
    birthday = models.DateField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    BMI = models.FloatField(null=True)

    def __str__(self):
        return self.studentname.username


class DailyActivity(models.Model):
    studentname = models.OneToOneField(
        User, on_delete=CASCADE, primary_key=True)
    step = models.IntegerField(null=True, blank=True)
    stepgoal = models.IntegerField(null=True, blank=True)
    stepvalue = models.IntegerField(null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    caloriesgoal = models.IntegerField(null=True, blank=True)
    caloriesvalue = models.IntegerField(null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    distancegoal = models.IntegerField(null=True, blank=True)
    distancevalue = models.IntegerField(null=True, blank=True)
    totalSteps = models.IntegerField(null=True, blank=True)
    totalCalories = models.IntegerField(null=True, blank=True)
    totalDistances = models.IntegerField(null=True, blank=True)
    hasValue = models.BooleanField(default=False, blank=True)
    goalSteps = models.IntegerField(null=True, blank=True)
    stride = models.IntegerField(null=True, blank=True)
    goalCalories = models.IntegerField(null=True, blank=True)
    heartRateSyncDate = models.DateField(null=True, blank=True)
    sleepSyncDate = models.DateField(null=True, blank=True)
    activitySyncDate = models.DateField(null=True, blank=True)
    mostStepsDate = models.DateField(null=True, blank=True)
    mostStepsValue = models.IntegerField(null=True, blank=True)
    achieveDays = models.IntegerField(null=True, blank=True)
    sleepScore = models.FloatField(null=True, blank=True)
    heartRatemax = models.FloatField(null=True, blank=True)
    heartRatemin = models.FloatField(null=True, blank=True)
    heartRateavg = models.FloatField(null=True, blank=True)
    date = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    yesterday_sleep = models.FloatField(null=True, default=0.00)
    yesterday_calories = models.FloatField(null=True, default=0.00)
    yesterday_steps = models.FloatField(null=True, default=0)
    today_sleep = models.FloatField(null=True, default=0.00)
    today_calories = models.FloatField(null=True, default=0.00)
    today_steps = models.FloatField(null=True, default=0.00)
    is_today_steps = models.BooleanField(default=False)
    is_today_sleep = models.BooleanField(default=False)
    is_today_calories = models.BooleanField(default=False)

    def __str__(self):
        return self.studentname.username


class Webdata(models.Model):
    Chart_types = [('pie', 'Pie'), ('bar', 'Bar'), ('line', 'Line')]
    studentname = models.OneToOneField(
        User, on_delete=CASCADE, primary_key=True)
    lesson1finish = models.IntegerField(default=0,
                                        validators=[MaxValueValidator(100), MinValueValidator(0)])
    lesson2finish = models.IntegerField(default=0,
                                        validators=[MaxValueValidator(100), MinValueValidator(0)])
    lesson3finish = models.IntegerField(default=0,
                                        validators=[MaxValueValidator(100), MinValueValidator(0)])
    is_lesson1_part1 = models.BooleanField(default=False)
    is_lesson1_part2 = models.BooleanField(default=False)
    is_lesson2_part1 = models.BooleanField(default=False)
    is_lesson2_part2 = models.BooleanField(default=False)
    is_lesson3_part1 = models.BooleanField(default=False)
    is_lesson3_part2 = models.BooleanField(default=False)
    chart_type = models.CharField(
        max_length=5, choices=Chart_types, default="line")

    def __str__(self):
        return self.studentname.username


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
