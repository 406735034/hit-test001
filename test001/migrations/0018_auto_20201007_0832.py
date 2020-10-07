# Generated by Django 2.2 on 2020-10-07 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test001', '0017_auto_20201006_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='webdata',
            name='studentname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
