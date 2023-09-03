from django.urls import path
from . import views
from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin
from ecom import views as ecom_views

urlpatterns = [
    path('', views.subscribe, name = 'subscribe'),
]