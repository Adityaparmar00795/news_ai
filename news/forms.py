from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['text', 'photo']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ( 'email', 'password1', 'password2')