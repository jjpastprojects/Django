# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-19 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0049_model2d'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='camera_upper_beta_limit',
            field=models.FloatField(default=1.5),
        ),
    ]
