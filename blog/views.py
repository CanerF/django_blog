from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author' : 'Caner',
        'title' : 'First post content',
        'content': 'This is my first content',
        'date_posted': '12.09.2020'
    },
    {
        'author' : 'Caner',
        'title' : 'Second post content',
        'content': 'This is my second content',
        'date_posted': '11.11.2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})