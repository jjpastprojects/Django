# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-18 22:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_profile_is_proxy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='user',
        ),
        migrations.DeleteModel(
            name='Personal',
        ),
    ]
