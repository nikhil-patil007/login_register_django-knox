from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/register_user',views.register_user),
    path('api/login_user',views.login_user),
]
