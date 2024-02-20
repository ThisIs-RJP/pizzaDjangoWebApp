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
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# cache = caches['redis']
# Create your views here.

def index(request):
    # Pizza.objects.all().delete() ## Deleting everything from testing
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
    orders = Pizza.objects.all().filter(author=request.user)
    return render(request, 'profile.html', {'orders' : orders})

def log_out(request):
    logout(request)
    return redirect("/")

@login_required(login_url='index') #redirect when user is not logged in
def order(request):
    if request.method == 'POST':
        toppings = request.POST.getlist("toppings")
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.author = request.user
            pizza.toppings = ", ".join(toppings)
            # pizza.toppings = "working"
            pizza.save()

            return redirect('index')
    else:
        form = PizzaForm()
        if form.is_valid():
            toppings = request.POST.getlist("toppings")
            pizza = form.save(commit=False)
            pizza.author = request.user
            pizza.toppings = ", ".join(toppings)
            # pizza.toppings = "working"
            pizza.save()

            return redirect('index')
    return render(request, 'order.html', {'form': form})

# def order(request):
#     if request.method == 'POST':
#         tops = request.POST.getlist("toppings")
#         form = PizzaForm(request.POST)
#         if form.is_valid():
            
#             # # Get the existing Pizza object if it exists
#             # pizza_instance = Pizza.objects.all()[0]

#             # # Update the existing Pizza object with the new data from the form
#             # pizza = form.save(commit=False)
#             # pizza.author = request.user
#             # pizza_instance.size = pizza.size
#             # pizza_instance.crust = pizza.crust
#             # pizza_instance.sauce = pizza.sauce
#             # pizza_instance.cheese = pizza.cheese
#             # pizza_instance.save()

#             return redirect('index')
#     else:
#         tops = request.POST.getlist("toppings")
#         form = PizzaForm()
#         if form.is_valid():
#             pizza = form.save(commit=False)
#             pizza.author = request.user
#             pizza.save()

#             return redirect('index')
#     return render(request, 'order.html', {'form': form})