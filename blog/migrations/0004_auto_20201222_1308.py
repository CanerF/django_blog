# Generated by Django 3.1.2 on 2020-12-22 10:08

import blog.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201220_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=20000, null=True, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default/default-photo.jpg', help_text='Fotoğraflarınızı Yükleyiniz', null=True, upload_to=blog.models.upload_to, verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Hikayenin Başlığı'),
        ),
    ]