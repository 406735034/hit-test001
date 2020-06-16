from django.db import models
from django.utils.timezone import timezone


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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)
    gender = models.BooleanField()

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class banddata(models.Model):
    username = models.TextField(null=False)
    password = models.TextField(null=False)
    male = models.TextField(null=True)
    female = models.TextField(null=True)
    data_time = models.TextField(null=True)
    userid = models.IntegerField(null=True)
    heart_recordnum = models.IntegerField(null=True)
    heart_max = models.IntegerField(null=True)
    heart_min = models.IntegerField(null=True)
    heart_total = models.IntegerField(null=True)
    sleep_deepsleeptime = models.IntegerField(null=True)
    sleep_lightsleeptime = models.IntegerField(null=True)
    sleep_awaketime = models.IntegerField(null=True)
    sleep_score = models.FloatField(null=True)
    sleep_waketimes = models.IntegerField(null=True)
    activity_totalsteps = models.IntegerField(null=True)
    activity_totalcalories = models.IntegerField(null=True)
    activity_totaldistances = models.IntegerField(null=True)
    activity_moststeps = models.IntegerField(null=True)
    sh150_light = models.IntegerField(null=True)
    sh150_moderate = models.IntegerField(null=True)
    sh150_vigorous = models.IntegerField(null=True)
    hasvalue = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.username


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.name


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

    def body_preview(self):
        return self.body[:50]


class Workout(models.Model):
    STATUS = (
        ('active', 'active'),
        ('used', 'used'),
        ('expired', 'expired')
    )
    banddata = models.ForeignKey(
        banddata, null=True, on_delete=models.SET_NULL)
    reward = models.ForeignKey(Reward, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS)


class Tamkang(models.Model):
    building = models.TextField(max_length=100, null=True)
    branches = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.building
