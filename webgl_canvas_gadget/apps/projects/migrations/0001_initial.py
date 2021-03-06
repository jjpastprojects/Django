# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-26 16:38
from __future__ import unicode_literals

import apps.projects.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pinax_stripe', '0002_auto_20151205_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=apps.projects.models.upload_to_projects_media)),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Plan')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
    ]
