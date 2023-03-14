from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',HomeScreen.as_view(template_name='blog/home.html' ),name="home"),
    path('<int:pk>/<str:slug>/',postDetails.as_view(template_name='blog/details.html' ),name="post-details"),
    # path('add/',AddPostScreen.as_view(),name="add-post"),
    # path('search/',SearchScreen.as_view(),name="search"),
]