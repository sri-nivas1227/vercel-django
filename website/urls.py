from django.contrib import admin
from django.urls import path
from .views import index, user, about

urlpatterns = [
    path('', index, name='index'),
    path('user', user, name='user'),
]
