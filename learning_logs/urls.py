from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', views.index, name='index'),  # para function-based view
    path('', views.index, name='index'),  # para class-based view
    path('topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]