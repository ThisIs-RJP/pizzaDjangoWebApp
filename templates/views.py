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
    return render(request, 'index.html')

def signup(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            form.save()
        return redirect(index)
    return render(request, 'signup.html')

# def upload(request):
#     if request.POST:
#         form = UploadForm(request.POST, request.FILES)
#         print(request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect(home)
#     return render(request, 'movies/upload.html', {'form' : UploadForm})