# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_directors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='directors',
        ),
    ]
