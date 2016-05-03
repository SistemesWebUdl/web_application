# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0036_auto_20160503_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='movies.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cities',
            field=models.ManyToManyField(blank=True, to='movies.City'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='companies',
            field=models.ManyToManyField(blank=True, to='movies.Company'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(blank=True, to='movies.Director'),
        ),
    ]
