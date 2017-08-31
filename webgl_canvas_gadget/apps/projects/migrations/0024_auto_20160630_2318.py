# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 17:18
from __future__ import unicode_literals

import apps.projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20160630_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skybox',
            name='nx',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_skybox_nx),
        ),
        migrations.AlterField(
            model_name='skybox',
            name='ny',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_skybox_ny),
        ),
        migrations.AlterField(
            model_name='skybox',
            name='nz',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_skybox_nz),
        ),
        migrations.AlterField(
            model_name='skybox',
            name='px',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_skybox_px),
        ),
        migrations.AlterField(
            model_name='skybox',
            name='py',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_skybox_py),
        ),
        migrations.AlterField(
            model_name='skybox',
            name='pz',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_skybox_pz),
        ),
        migrations.AlterField(
            model_name='skybox',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_skybox_thumbnail),
        ),
    ]
