from django.db.models.signals import *
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(studentname=instance)
        Webdata.objects.create(studentname=instance)
        a = StudentProfile.objects.get(studentname=instance)
        a.photo = "female"
        a.save()


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.studentprofile.save()
        instance.webdata.save()


# @receiver(post_save, sender=DailyActivity)
# def ranking(sender, instance, created, **kwargs):
#     if created == False:
#         steplist = DailyActivity.objects.get(instance.steps)
