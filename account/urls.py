from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=UserLoginForm), name='login'),

]
