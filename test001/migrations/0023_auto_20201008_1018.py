# Generated by Django 2.2 on 2020-10-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test001', '0022_auto_20201007_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='Class',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='School',
            field=models.CharField(default='淡江大學', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='Section',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
