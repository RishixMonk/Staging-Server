from django import forms
from django.forms import ModelForm
from .models import Info

class Infoform(ModelForm):
    class Meta:
        model=Info
        fields="__all__"