from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User





class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': "form-input"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-input"}))