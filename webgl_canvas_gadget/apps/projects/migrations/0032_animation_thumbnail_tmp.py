# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-24 14:19
from __future__ import unicode_literals

import apps.projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_auto_20160717_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='animation',
            name='thumbnail_tmp',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_animation_to_media),
        ),
    ]
