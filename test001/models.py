from datetime import date
from os import name
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.utils.timezone import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    Gender_Choices = [(1, 'Male'), (2, 'Female')]
    studentname = models.OneToOneField(User, on_delete=models.CASCADE,
                                       primary_key=True)
    gender = models.CharField(choices=Gender_Choices,
                              max_length=2, default='2')
    School = models.CharField(max_length=30, null=True, default="大同國小")
    SchoolId = models.IntegerField(default=4576)
    photo = models.ImageField(null=True, blank=True,
                              default="naa.png")
    account = models.CharField(max_length=100)
    userId = models.CharField(max_length=255)
    birthday = models.IntegerField(default=0)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    BMI = models.FloatField(null=True)

    Class = models.CharField(max_length=30, null=True)
    Section = models.CharField(max_length=30, null=True)
    RollNo = models.IntegerField(default=0)

    def __str__(self):
        return self.studentname.username


class DailyActivity(models.Model):
    class Meta(object):
        unique_together = (("act_date", "user"), )
    steps = models.IntegerField(default=0)
    stepsgoal = models.IntegerField(default=1)
    calories = models.IntegerField(default=0)
    caloriesgoal = models.IntegerField(default=1)
    totaldistance = models.IntegerField(default=0)
    heartmin = models.IntegerField(default=0)
    heartmax = models.IntegerField(default=0)
    hearttotal = models.IntegerField(default=0)
    recordNum = models.IntegerField(default=0)
    hasvalue = models.BooleanField(default=False)
    sleepscore = models.FloatField(default=0.00)
    act_date = models.DateField()
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.sleepscore = round(self.sleepscore, 2)
        super(DailyActivity, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s' % (self.user.studentname.first_name, self.act_date)

# class Act(models.Model):
#     class Meta(object):
#         unique_together = (("date", "student", "activity"), )
#     date = models.DateField(db_index=True, default=datetime.date.today)
#     student = models.ForeignKey(User, on_delete=CASCADE)
#     activity = models.(DailyActivity, on_delete=CASCADE)

#     def __str__(self):
#         return (str(self.date))


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


class Class(models.Model):
    classname = models.CharField(max_length=200, null=True)
    # Teacher = models.OneToOneField


class Datetest(models.Model):
    date = models.DateField(
        primary_key=True, default=datetime.date.today)
