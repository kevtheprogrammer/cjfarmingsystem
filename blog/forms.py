from django import forms
from django.forms import ModelForm

from .models import *

class PostForm(ModelForm):
	class Meta:
		model = Article
		fields = (
			'title',
			'thumb',
			'cat',
            'upload',
			'intro', 
			'body', 
			'v_link', 
			'm_link',
			's_link',          
			)
		widgets = {
		'cat': forms.RadioSelect(),
		'thumb': forms.ClearableFileInput(),
		}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')