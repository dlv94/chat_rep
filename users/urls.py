from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register, name='register'),
    #re_path(r'^login/$', login(template_name='login.html'), name='login'),
]