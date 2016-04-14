# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20160414_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='directors',
        ),
        migrations.AddField(
            model_name='director',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
    ]
