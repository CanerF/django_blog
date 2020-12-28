from django.urls import path
from . import views
from django.conf.urls import url
from .views import post_create,post_list
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^post_list/$', post_list, name='post_list'),

    url(r'^post_create/$', post_create ,name='post_create'),
       
    url('',views.home, name='blog-home'),

    url('about/', views.about, name='blog-about'),


]