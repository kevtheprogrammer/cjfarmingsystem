from django.urls import path,include

from .views import SignUpView,ActivateAccount

app_name = 'account'

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("signup/", SignUpView.as_view(),name="signup"),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

]

 
 