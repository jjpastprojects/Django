# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-11 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_profile_follow_process_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='follow_process_complete',
            new_name='follow_process_is_complete',
        ),
    ]
