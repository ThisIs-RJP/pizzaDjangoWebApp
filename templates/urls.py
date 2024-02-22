from django.urls import path
from . import views
from .forms import *
# from .views import SignUpView

urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('create', views.signup, name="makeAccount"),
    # path('log-in', views.LoginView.as_view(template_name="logIn.html", authentication_form=UserLoginForm), name="logIn"),
    path('login', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
    path('logout/', views.log_out, name="logout"),
    path('order', views.order, name="order"),
    path('delivery', views.delivery, name="delivery"),
]