# Generated by Django 3.1.2 on 2021-01-06 09:31

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210101_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_2',
            field=models.ImageField(blank=True, default='default/default-photo.jpg', help_text=' Fotoğraflarınızı Yükleyiniz', null=True, upload_to=blog.models.upload_to, verbose_name='Fotoğraflar'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_3',
            field=models.ImageField(blank=True, default='default/default-photo.jpg', help_text=' Fotoğraflarınızı Yükleyiniz', null=True, upload_to=blog.models.upload_to, verbose_name='Fotoğraflar'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_4',
            field=models.ImageField(blank=True, default='default/default-photo.jpg', help_text=' Fotoğraflarınızı Yükleyiniz', null=True, upload_to=blog.models.upload_to, verbose_name='Fotoğraflar'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_5',
            field=models.ImageField(blank=True, default='default/default-photo.jpg', help_text=' Fotoğraflarınızı Yükleyiniz', null=True, upload_to=blog.models.upload_to, verbose_name='Fotoğraflar'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_city',
            field=models.CharField(max_length=100, null=True, verbose_name='Şehir'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_country',
            field=models.CharField(max_length=100, null=True, verbose_name='Ülke'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default/default-photo.jpg', help_text=' Fotoğraflarınızı Yükleyiniz', null=True, upload_to=blog.models.upload_to, verbose_name='Fotoğraflar'),
        ),
    ]