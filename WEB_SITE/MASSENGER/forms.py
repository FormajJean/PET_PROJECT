from django.forms import ModelForm
from django.forms.widgets import Select, Textarea
from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import *

class PPLForms(forms.ModelForm):
    last_name = forms.CharField(label = 'Фамилия', widget = forms.TextInput(attrs = {'class' : 'form-input'}))
    first_name = forms.CharField(label = 'Имя', widget = forms.TextInput(attrs = {'class' : 'form-input'}))
    surname = forms.CharField(label = 'Отчество', widget = forms.TextInput(attrs = {'class' : 'form-input'}))
    age = forms.CharField(label = 'Возраст', required = False, widget = forms.TextInput(attrs = {'class' : 'form-input'}))
    profession = forms.CharField(label = 'Профессия', widget = forms.TextInput(attrs = {'class' : 'form-input'}))
    what_are_you_looking = forms.ChoiceField(label = 'Что вы ищите', choices = PPL.Kinds,)
    image = forms.FileField(label = 'Фотография', required = False)
    region = forms.ModelChoiceField(queryset = Region.objects.all(), label = 'Регион', required = False)
    information_about_skills = forms.CharField(label = 'Иноформация об профессиональных качествах', widget = forms.Textarea(), required = False)

    class Meta:
        model = PPL
        fields = ('last_name', 'first_name', 'surname', 'age', 'profession', 'what_are_you_looking', 'image', 'region', 'information_about_skills')
