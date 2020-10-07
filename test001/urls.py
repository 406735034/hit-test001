from django.conf.urls import include
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    # Index
    path('', views.home, name='home'),
    # Login
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    # Reset Password
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name="password_reset_complete"),

    # Home
    path('dashboard/', views.dashboard, name='dashboard'),

    # User
    path('user/', views.userPage, name='user-page'),
    path('user-rec/', views.userRecPage, name='user-rec'),
    path('user-awards/', views.userAwards, name='user-awards'),
    path('user-ranks/', views.userRanks, name='user-ranks'),
    # Warnings
    path('restrict/', views.restrict, name='restrict'),

    path('route/', include(router.urls)),
]
