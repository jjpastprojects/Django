# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-21 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0050_project_camera_upper_beta_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='animation',
            name='external_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
