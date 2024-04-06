from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Post(models.Model):
    title = models.CharField(max_length=450) #Заголовок поста
    author = models.ForeignKey( #Автор поста
        'auth.User',
        on_delete=models.CASCADE, #Удаление поста
    )
    body = models.TextField() #Поле поста

    def __str__(self): #Метод
        return self.title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': "form-input"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': "form-input"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-input"}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': "form-input"}))
    model = User
    fields = ('username', 'email', 'password1', 'password2')





