from django.forms import ModelForm
from django import forms
from .models import Pizza

class UploadForm(ModelForm):
    name = forms.TextInput()
    desc = forms.TextInput()
    class Meta:
        model = Pizza
        fields = ['name', 'desc']