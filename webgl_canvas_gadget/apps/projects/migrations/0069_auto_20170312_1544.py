# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-12 09:44
from __future__ import unicode_literals

from django.db import migrations

def subscription_field_data_migration(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Subscription = apps.get_model("pinax_stripe", "Subscription")
    for o in Project.objects.all():
        s = None
        try:
            if o.owner:
                s = Subscription.objects.get(plan=o.plan, customer__user=o.owner)
        except Subscription.DoesNotExist:
            pass
        
        o.subscription_field = s
        o.save()

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0068_project_subscription_field'),
        ('pinax_stripe', '0006_coupon'),
    ]

    operations = [
        migrations.RunPython(subscription_field_data_migration),
    ]
