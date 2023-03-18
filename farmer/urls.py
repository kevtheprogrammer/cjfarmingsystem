from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required

from .views import  AdminView, FarmerDetiails,MakeReport,ViewReport,RegistraionView

app_name = 'farmer'

urlpatterns = [
    path("",login_required(AdminView.as_view()) ,name='index'),
    path("farmer/",login_required(FarmerDetiails.as_view()),name = 'f_details'),
    path("registration/",login_required(RegistraionView.as_view()),name = 'registration'),
    path("report/",login_required(ViewReport.as_view()),name = 'report'),
    path("report/<int:pk>/",login_required(MakeReport.as_view()),name = 'add_report'),
]

