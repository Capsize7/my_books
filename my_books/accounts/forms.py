from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_summernote.widgets import SummernoteWidget

from .models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={"class": "form-control mb-1"}), label='Имя')
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={"class": "form-control mb-1"}), label="Фамилия")
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control mb-1"}), label='Имя пользователя')
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "form-control mb-1"}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control mb-1"}),
                                label='Пароль')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control mb-1"}),
                                label='Подтвердите пароль')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': "form-control mb-1"}), label='Имя пользователя')
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control mb-1"}), label='Пароль')
    remember_me = forms.BooleanField(required=False, label='Запомнить меня')

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control mb-1"}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={"class": "form-control mb-1"}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control mb-1", 'placeholder': 'Аватар'}))
    bio = forms.CharField(widget=SummernoteWidget(attrs={"class": "form-control", 'placeholder': 'Расскажите о себе',
                                                         'summernote': {'width': '100%', 'height': '300px'}}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
