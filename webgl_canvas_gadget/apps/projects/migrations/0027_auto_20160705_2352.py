# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-05 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_linestyle_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='callout',
            name='x',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='callout',
            name='y',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='callout',
            name='z',
            field=models.FloatField(default=0.0),
        ),
    ]
