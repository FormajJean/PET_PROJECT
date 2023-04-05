from django.forms import ModelForm
from django import forms
from .models import *

class PPLForms(forms.ModelForm):
    first_name = forms.CharField(label = 'Имя ')
    class Meta:
        model = PPL
        fields = ('__all__')