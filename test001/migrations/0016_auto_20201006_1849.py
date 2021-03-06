# Generated by Django 2.2 on 2020-10-06 10:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test001', '0015_dailyactivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson1finish', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('lesson2finish', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('lesson3finish', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('is_lesson1_part1', models.BooleanField(default=False)),
                ('is_lesson1_part2', models.BooleanField(default=False)),
                ('is_lesson2_part1', models.BooleanField(default=False)),
                ('is_lesson2_part2', models.BooleanField(default=False)),
                ('is_lesson3_part1', models.BooleanField(default=False)),
                ('is_lesson3_part2', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='today_calories',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='today_sleep',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='today_steps',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='yesterday_calories',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='yesterday_sleep',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='yesterday_steps',
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='is_today_calories',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='is_today_sleep',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='is_today_steps',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='today_calories',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='today_sleep',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='today_steps',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='yesterday_calories',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='yesterday_sleep',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='yesterday_steps',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.DeleteModel(
            name='banddata',
        ),
    ]
