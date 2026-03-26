from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', views.chat, name='chat'),
]