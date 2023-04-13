from django.forms import ModelForm
from django.forms.widgets import Select, Textarea
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class PPLForms(forms.ModelForm):
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-input'}))
    age = forms.CharField(label='Возраст', required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    profession = forms.CharField(label='Профессия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    what_are_you_looking = forms.ChoiceField(label='Что вы ищите', choices=PPL.Kinds, )
    image = forms.FileField(label='Фотография', required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label='Регион', required=False)
    information_about_skills = forms.CharField(label='Иноформация об профессиональных качествах',
                                               widget=forms.Textarea(), required=False)

    class Meta:
        model = PPL
        fields = ('last_name', 'first_name', 'surname', 'age', 'profession', 'what_are_you_looking', 'image', 'region',
                  'information_about_skills')


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs= {'class' : 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginAuthenticatedForm(AuthenticationForm):
    username = forms.CharField(label = 'Логин', widget = forms.TextInput(attrs={'class' : 'form-input'}))
    password = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs={'class' : 'form-input'}))