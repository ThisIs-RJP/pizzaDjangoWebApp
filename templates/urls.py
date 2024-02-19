from django.urls import path
from . import views
<<<<<<< HEAD
from .views import SignUpView

urlpatterns = [
    path('', views.index, name="index"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('error', views.signup, name="error"),
    path('success', views.signup, name="success"),
=======
from .forms import *
# from .views import SignUpView

urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('create', views.signup, name="makeAccount"),
    path('log-in', views.LoginView.as_view(template_name="logIn.html", authentication_form=UserLoginForm), name="logIn"),
    path('logout/', views.log_out, name="logout"),
    path('order', views.order, name="order"),
>>>>>>> refs/remotes/origin/main
]