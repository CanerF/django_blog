# Generated by Django 3.1.2 on 2020-12-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201222_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='unique_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
