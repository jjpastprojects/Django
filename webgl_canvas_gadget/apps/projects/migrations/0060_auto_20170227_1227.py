# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0059_project_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='popup_position_top',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AddField(
            model_name='project',
            name='popup_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='popup_text',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='popupp_position_left',
            field=models.PositiveIntegerField(default=50),
        ),
    ]
