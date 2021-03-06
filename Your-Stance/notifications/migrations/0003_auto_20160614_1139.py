# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20160520_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('RS', 'Reply to stance comment'), ('RF', 'Reply to forum comment'), ('AG', 'Agreed with your stance'), ('LI', 'Liked your comment'), ('MT', 'Mentioned your name')], default='RS', max_length=2),
        ),
    ]
