# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20160414_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]