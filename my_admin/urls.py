from django.contrib import admin
from django.urls import path
from my_admin import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
]
