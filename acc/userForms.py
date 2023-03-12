from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
 

from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'email', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2', 
            ]