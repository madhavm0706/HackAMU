from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user/login/',views.UserLogin,name='ulogin'),
    path('police/login',views.PoliceLogin,name='plogin'),
    
]