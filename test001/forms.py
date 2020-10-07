from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class ResetForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email']


class StudentForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = "__all__"
        exclude = ['studentname']
