# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-12-08 10:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181208_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysearch',
            name='publish_data',
        ),
    ]
