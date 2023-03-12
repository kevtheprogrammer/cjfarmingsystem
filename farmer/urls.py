from django.contrib import admin
from django.urls import path,include

from .views import  AdminView
app_name = 'farmer'

urlpatterns = [
    path("",AdminView.as_view() ,name='index'),
]

