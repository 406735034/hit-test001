# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bandsdata(models.Model):
    username = models.TextField(blank=True, null=True)
    password = models.BigIntegerField(blank=True, null=True)
    male = models.FloatField(blank=True, null=True)
    female = models.FloatField(blank=True, null=True)
    data_time = models.TextField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    heart_recordnum = models.BigIntegerField(db_column='heart_recordNum', blank=True, null=True)  # Field name made lowercase.
    heart_max = models.BigIntegerField(blank=True, null=True)
    heart_min = models.BigIntegerField(blank=True, null=True)
    heart_total = models.BigIntegerField(blank=True, null=True)
    sleep_deepsleeptime = models.BigIntegerField(db_column='sleep_deepSleepTime', blank=True, null=True)  # Field name made lowercase.
    sleep_lightsleeptime = models.BigIntegerField(db_column='sleep_lightSleepTime', blank=True, null=True)  # Field name made lowercase.
    sleep_awaketime = models.BigIntegerField(db_column='sleep_awakeTime', blank=True, null=True)  # Field name made lowercase.
    sleep_score = models.FloatField(blank=True, null=True)
    sleep_waketimes = models.BigIntegerField(db_column='sleep_wakeTimes', blank=True, null=True)  # Field name made lowercase.
    activity_totalsteps = models.BigIntegerField(db_column='activity_totalSteps', blank=True, null=True)  # Field name made lowercase.
    activity_totalcalories = models.BigIntegerField(db_column='activity_totalCalories', blank=True, null=True)  # Field name made lowercase.
    activity_totaldistances = models.BigIntegerField(db_column='activity_totalDistances', blank=True, null=True)  # Field name made lowercase.
    activity_moststeps = models.BigIntegerField(db_column='activity_mostSteps', blank=True, null=True)  # Field name made lowercase.
    sh150_light = models.BigIntegerField(blank=True, null=True)
    sh150_moderate = models.BigIntegerField(blank=True, null=True)
    sh150_vigorous = models.BigIntegerField(blank=True, null=True)
    hasvalue = models.IntegerField(db_column='hasValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bandsdata'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
