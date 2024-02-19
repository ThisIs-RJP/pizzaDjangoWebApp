from django.shortcuts import *
from django.http import *
from templates.forms import *
from templates.models import *
from django.core.cache import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

# cache = caches['redis']
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'makeAccount.html', {'form': form})

class UserLoginView(LoginView):
    template_name='logIn.html'

def profile(request):
    return render(request, 'profile.html')

def log_out(request):
    logout(request)
    return redirect("/")

def order(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.author = request.user
            pizza.save()
            return redirect('index')
    else:
        form = PizzaForm()
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.author = request.user
            pizza.save()
            return redirect('index')
    return render(request, 'order.html', {'form': form})
