# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-12-03 15:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181203_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysearch',
            name='filename',
            field=models.FileField(default=datetime.datetime(2018, 12, 3, 15, 23, 48, 54000, tzinfo=utc), upload_to='./file/'),
            preserve_default=False,
        ),
    ]