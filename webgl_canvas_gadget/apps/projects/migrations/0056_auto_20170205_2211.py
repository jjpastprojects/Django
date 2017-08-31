# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-05 16:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0055_project_light'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='source',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[{'color': {'diffuse': {'b': 1, 'g': 1, 'r': 1}, 'groundColor': {'b': 1, 'g': 1, 'r': 1}, 'specular': {'b': 1, 'g': 1, 'r': 1}}, 'intensity': 1, 'position': {'x': 0, 'y': 1, 'z': 0}, 'range': 1, 'type': 'HemisphericLight'}, {'diffuse': {'b': 1, 'g': 1, 'r': 1}, 'direction': {'x': 0, 'y': 1, 'z': 0}, 'groundColor': {'b': 1, 'g': 1, 'r': 1}, 'intensity': 0.4, 'position': {'x': 0, 'y': -5, 'z': 0}, 'range': 5, 'specular': {'b': 1, 'g': 1, 'r': 1}, 'type': 'DirectionalLight'}, {'diffuse': {'b': 1, 'g': 1, 'r': 1}, 'groundColor': {'b': 1, 'g': 1, 'r': 1}, 'intensity': 1, 'position': {'x': 0, 'y': -1, 'z': 0}, 'range': 1, 'specular': {'b': 1, 'g': 1, 'r': 1}, 'type': 'HemisphericLight'}]),
        ),
    ]
