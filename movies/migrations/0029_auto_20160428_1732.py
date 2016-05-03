# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 17:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0028_auto_20160428_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=40)),
                ('zipCode', models.TextField(blank=True, null=True)),
                ('stateOrProvince', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='country',
            name='user',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='country',
        ),
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.RemoveField(
            model_name='director',
            name='country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='countries',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.AddField(
            model_name='actor',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.City'),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.City'),
        ),
        migrations.AddField(
            model_name='director',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.City'),
        ),
        migrations.AddField(
            model_name='movie',
            name='cities',
            field=models.ManyToManyField(blank=True, null=True, to='movies.City'),
        ),
    ]
