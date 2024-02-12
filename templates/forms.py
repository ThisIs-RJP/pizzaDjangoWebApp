from django import forms
from .models import *
from django.contrib.auth.forms import *
from django.db import *

class UploadForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']

class SignUp(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["username",
                  "email",
                  "password"]