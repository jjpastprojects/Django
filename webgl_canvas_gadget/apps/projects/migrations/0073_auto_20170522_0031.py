# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-21 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0072_model3dgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model3dgallery',
            options={'ordering': ['numv', 'numh'], 'verbose_name': '3d model gallery', 'verbose_name_plural': '3d model galleries'},
        ),
        migrations.AddField(
            model_name='animation',
            name='auto_reverse',
            field=models.BooleanField(default=True),
        ),
    ]
