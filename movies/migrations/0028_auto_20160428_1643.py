# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 16:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0027_auto_20160428_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='city',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='stateOrProvince',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='zipCode',
        ),
    ]