# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentmanager', '0004_author_is_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50, verbose_name='Фамилия'), unique=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]