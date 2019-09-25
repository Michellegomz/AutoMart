from django.contrib import admin
from django.urls import path
from . import views                     #importamos la vista de main app



urlpatterns = [
    path('', views.index),              #Es el archivo views y hace a funcion de index
]