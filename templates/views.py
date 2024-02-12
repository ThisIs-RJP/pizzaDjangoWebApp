from django.shortcuts import *
from django.http import *
from templates.forms import *
from templates.models import *
from django.core.cache import *

# cache = caches['redis']

# Create your views here.

def home(request):
    return HttpResponse("ok")

def index(request):
    # Pizza.objects.all().delete() ## Deleting everything from testing
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
    return render(request, 'signup.html', {'form' : UploadForm})

# def upload(request):
#     if request.POST:
#         form = UploadForm(request.POST, request.FILES)
#         print(request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect(home)
#     return render(request, 'movies/upload.html', {'form' : UploadForm})