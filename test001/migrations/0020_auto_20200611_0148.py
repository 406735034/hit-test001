# Generated by Django 3.0.7 on 2020-06-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test001', '0019_auto_20200611_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='workout',
            name='tags',
            field=models.ManyToManyField(to='test001.Tag'),
        ),
    ]
