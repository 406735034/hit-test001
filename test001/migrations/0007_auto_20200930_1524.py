# Generated by Django 2.2 on 2020-09-30 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test001', '0006_dailyactivity_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Tamkang',
        ),
        migrations.DeleteModel(
            name='userdata',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
