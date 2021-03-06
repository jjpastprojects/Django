# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-20 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('slug', models.SlugField()),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('website_screenshot', models.ImageField(upload_to='demobooth')),
                ('website_extra_html', tinymce.models.HTMLField(default='<iframe src="" frameborder="0" width="256" height="256"></iframe>', max_length=2048)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
