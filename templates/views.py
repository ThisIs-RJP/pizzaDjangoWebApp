from django.shortcuts import *
from django.http import *
from templates.forms import *
from templates.models import *
from django.core.cache import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# cache = caches['redis']

# Create your views here.

def home(request):
    return HttpResponse("ok")

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = UploadForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            return render(request, 'success.html', {'pizza' : pizza })
        else:
            print("Failed!")
            return redirect(index)
            # return render(request, '')
    return render(request, 'makeAccount.html', {'form' : UploadForm})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("success.html")
    template_name = "makeAccount.html"

# def upload(request):
#     if request.POST:
#         form = UploadForm(request.POST, request.FILES)
#         print(request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect(home)
#     return render(request, 'movies/upload.html', {'form' : UploadForm})