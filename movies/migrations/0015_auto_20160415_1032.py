# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 10:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0014_auto_20160415_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='company',
            name='movies',
            field=models.ManyToManyField(related_name='companies', to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
