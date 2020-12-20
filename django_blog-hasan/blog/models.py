from django.db import models
from django.shortcuts import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify, safe
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from uuid import uuid4
import os
from ckeditor.fields import RichTextField




def upload_to(instance, filename):
    uzanti = filename.split('.')[-1]
    new_name = "%s.%s" % (str(uuid4()), uzanti)
    unique_id = instance.unique_id
    return os.path.join('blog', unique_id, new_name)

class Post(models.Model):
    title =models.CharField(max_length=100, blank=False, null=True, verbose_name='Başlık Giriniz',
                             help_text='Başlık Bilgisi Burada Girilir.')
    content =RichTextField(null=True, blank=False, max_length=5000, verbose_name='İçerik')
    slug = models.SlugField(null=True, unique=True, editable=False)

    date_posted =models.DateField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=1, null=True, verbose_name='User', related_name='blog')
    image = models.ImageField(default='default/default-photo.jpg', upload_to=upload_to, blank=True,
                              verbose_name='Resim',
                              null=True,
                              help_text='Kapak Fotoğrafı Yükleyiniz')
    class Meta:
        verbose_name_plural = 'Gönderiler'
        ordering = ['-id']

    def __str__(self):
        return "%s %s" % (self.title, self.user)

    def get_absolute_url(self):
        return reverse('post_crate', kwargs={'slug': self.slug})


    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Blog.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s" % (slug, sayi)

        slug = new_slug
        return slug    




    



