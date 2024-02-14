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
# def signup(request):
#     if request.method == "POST":
#         form = UploadForm(request.POST)
#         if form.is_valid():
#             pizza = form.save()
#             return render(request, 'success.html', {'pizza' : pizza })
#         else:
#             print("Failed!")
#             return redirect(index)
#     return render(request, 'makeAccount.html', {'form' : UploadForm})

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("success.html")
#     template_name = "makeAccount.html"