from django.urls import path
from . import views
from django.conf.urls import url
from .views import post_create,post_list

urlpatterns = [

    url(r'^post_create/$', post_create ,name='post_create'),
    url(r'^post_list/(?P<slug>[-\w]+)/$', post_list, name='post_list'),
       
    url('',views.home, name='blog-home'),

    url('about/', views.about, name='blog-about'),


]