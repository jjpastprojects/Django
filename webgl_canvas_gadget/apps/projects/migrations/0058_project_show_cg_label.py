# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0057_material_normal_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='show_cg_label',
            field=models.BooleanField(default=True),
        ),
    ]
