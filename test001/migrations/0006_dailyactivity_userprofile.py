# Generated by Django 2.2 on 2020-09-30 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('test001', '0005_delete_postmandb'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyActivity',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('hasValue', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(default=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL), max_length=32)),
                ('gender', models.IntegerField(choices=[('1', 'Male'), ('2', 'Female')], default='1')),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('email', models.EmailField(max_length=255)),
                ('account', models.CharField(max_length=100)),
                ('userId', models.CharField(max_length=255)),
            ],
        ),
    ]
