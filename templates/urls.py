from django.urls import path
from . import views
from .forms import *
# from .views import SignUpView

urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('create', views.signup, name="makeAccount"),
    path('log-in', views.LoginView.as_view(template_name="logIn.html", authentication_form=UserLoginForm), name="logIn"),
    path('logout/', views.log_out, name="logout"),
    path('testing/', views.testing, name="testing"),
]