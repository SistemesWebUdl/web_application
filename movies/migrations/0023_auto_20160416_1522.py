# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_auto_20160416_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(blank=True, to='movies.Country', null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='country',
            field=models.ForeignKey(blank=True, to='movies.Country', null=True),
        ),
    ]
