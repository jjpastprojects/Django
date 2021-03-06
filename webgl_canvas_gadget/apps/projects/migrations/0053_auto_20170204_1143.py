# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 05:43
from __future__ import unicode_literals

import apps.projects.models
from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0052_auto_20170122_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animation',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, default='', null=True, upload_to=apps.projects.models.upload_animation_to_media),
        ),
        migrations.AlterField(
            model_name='animation',
            name='thumbnail_tmp',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, default='', null=True, upload_to=apps.projects.models.upload_animation_to_media),
        ),
    ]
