# Generated by Django 4.0.4 on 2022-05-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
