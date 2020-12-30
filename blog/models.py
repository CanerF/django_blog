from django.db import models
from django.shortcuts import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify, safe
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils import timezone

from uuid import uuid4
import os
from ckeditor.fields import RichTextField




def upload_to(instance, filename):
    uzanti = filename.split('.')[-1]
    new_name = "%s.%s" % (str(uuid4()), uzanti)
    unique_id = instance.unique_id
    return os.path.join('blog', unique_id, new_name)

class Post(models.Model):
    title =models.CharField(max_length=50, blank=False, null=True, verbose_name='Hikayenin Başlığı',
                             help_text='')
    content_country =models.CharField(null=True, blank=False, max_length=100, verbose_name='Gidilen Ülke')
    content_city =models.CharField(null=True, blank=False, max_length=100, verbose_name='Gidilen Şehir')

               
    content_cost =RichTextField(null=True, blank=False, max_length=20000, verbose_name='Harcama')
    content_food= RichTextField(null=True, blank=False, max_length=20000, verbose_name='Yemekler')
    content_fun= RichTextField(null=True, blank=False, max_length=20000, verbose_name='Eğlence')
    content_transportation= RichTextField(null=True, blank=False, max_length=20000, verbose_name='Ulaşım')
    content_visit= RichTextField(null=True, blank=False, max_length=20000, verbose_name='Gezilecek Yerler')
    content_cities= RichTextField(null=True, blank=False, max_length=20000, verbose_name='Gezdiğim Diğer Şehirler')
    content_education= RichTextField(null=True, blank=False, max_length=20000, verbose_name='Eğitim ve Okul Hayatı')
    content_hint= RichTextField(null=True, blank=False, max_length=20000, verbose_name='İpuçları')



    slug = models.SlugField(null=True, unique=True, editable=False)

    date_posted = models.DateField(default=timezone.now)
    image = models.ImageField( default='default/default-photo.jpg', upload_to=upload_to, blank=True,
                              verbose_name='Fotoğraflar',
                              null=True,
                              help_text='Kapak Fotoğrafı Yükleyiniz')
    author = models.CharField(max_length=100,blank=False,null=True,verbose_name="Yazar")
    unique_id = models.CharField(max_length=100, editable=False, null=True)

   
    class Meta:
        verbose_name_plural = 'Gönderiler'
        ordering = ['-id']
  
  
    def get_image(self):
        if self.image:
            print(self.image.url)
            return self.image.url
        else:
            return '/media/default/default-photo.jpg'

    def __str__(self):
        return "%s %s" % (self.title, self.author)

    def get_absolute_url(self):
        return reverse('blog-home') #,kwargs={'slug': self.slug})

    

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Post.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s" % (slug, sayi)

        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id
            self.slug = self.get_unique_slug()
        else:
            post = Post.objects.get(slug=self.slug)
            if post.title != self.title:
                self.slug = self.get_unique_slug()
        print(self.title)
        super(Post, self).save(*args, **kwargs)


    



