# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentmanager', '0003_author_new_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_winner',
            field=models.BooleanField(default=False),
        ),
    ]
