# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-12-20 14:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20181218_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysearch',
            name='publish_data',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 20, 14, 43, 56, 809000, tzinfo=utc)),
        ),
    ]
