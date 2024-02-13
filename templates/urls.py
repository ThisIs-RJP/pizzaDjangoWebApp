from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name="index"),
    # path('signup', views.signup, name="signup"),
    path('signup', SignUpView.as_view(), name="signup"),
    path('error', views.signup, name="error"),
    path('success', views.signup, name="success"),
]