from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, reverse, Http404
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.template.loader import render_to_string
from .forms import BlogForm

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

def post_create(request):
   
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            msg = "Tebrikler <strong> %s </strong> isimli gönderiniz başarıyla oluşturuldu." % (blog.title)
            messages.success(request, msg, extra_tags='success')
            # reverse('post-detail', kwargs={'pk': blog.pk})
            return HttpResponseRedirect(blog.get_absolute_url())
    return render(request, 'blog/post_create.html', context={'form': form})