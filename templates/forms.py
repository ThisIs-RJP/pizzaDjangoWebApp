from django import forms
from .models import *
<<<<<<< HEAD
from django.contrib.auth.forms import *
from django.db import *
=======
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
>>>>>>> refs/remotes/origin/main

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    password1 = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label= ("Confirm Password"),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
        help_texts = {
            'username': None,
            'email': None,
            'password1' : None,
            'password2' : None,
        }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = ['color']

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
<<<<<<< HEAD
        fields = ['name']

class SignUp(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["username",
                  "email",
                  "password"]
=======
        fields = ["size",
                  "crust",
                  "sauce",
                  "cheese"
                  ]
>>>>>>> refs/remotes/origin/main
