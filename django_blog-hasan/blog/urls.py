from django.urls import path
from . import views
from django.conf.urls import url
from .views import post_create

urlpatterns = [
    url('', views.home, name='blog-home'),
    url('about/', views.about, name='blog-about'),
    url('admin/', views.about, name='blog-admin'),
    url(r'^post_create/$', post_create, name='post_create'),

]