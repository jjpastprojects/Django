# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0054_light'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='light',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.Light'),
        ),
    ]
