# Generated by Django 2.2 on 2020-10-06 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test001', '0011_auto_20201006_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='user',
            new_name='studentname',
        ),
    ]
