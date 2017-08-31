# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-26 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_project_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnchorStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('image', models.ImageField(upload_to='projects/style/anchor')),
            ],
            options={
                'verbose_name': 'anchor style',
                'ordering': ['id'],
                'verbose_name_plural': 'anchor styles',
            },
        ),
        migrations.CreateModel(
            name='Callout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('label', models.CharField(max_length=40)),
                ('text', models.CharField(max_length=80)),
                ('anchor_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.AnchorStyle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CalloutStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('image', models.ImageField(upload_to='projects/style/callout')),
            ],
            options={
                'verbose_name': 'callout style',
                'ordering': ['id'],
                'verbose_name_plural': 'callout styles',
            },
        ),
        migrations.CreateModel(
            name='LineStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('image', models.ImageField(upload_to='projects/style/line')),
            ],
            options={
                'verbose_name': 'line style',
                'ordering': ['id'],
                'verbose_name_plural': 'line styles',
            },
        ),
        migrations.AddField(
            model_name='callout',
            name='callout_style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.CalloutStyle'),
        ),
        migrations.AddField(
            model_name='callout',
            name='line_style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.LineStyle'),
        ),
        migrations.AddField(
            model_name='callout',
            name='model3d',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Model3D'),
        ),
    ]
