from django.urls import path
from . import views
from django.conf.urls import url
from .views import post_create,post_list
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^post_list/(?P<slug>[-\w]+)/$', post_list, name='post_list'),

    url(r'^post_create/$', post_create ,name='post_create'),
       
    url(r'^$',views.home, name='blog-home'),

    url('about/', views.about, name='blog-about')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
