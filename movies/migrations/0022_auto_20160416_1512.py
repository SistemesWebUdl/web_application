# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_auto_20160415_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='country',
            field=models.ForeignKey(default=1, to='movies.Country'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
