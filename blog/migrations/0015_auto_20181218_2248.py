# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-12-18 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20181217_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysearch',
            name='file',
            field=models.FileField(blank=True, upload_to='./file/'),
        ),
        migrations.AlterField(
            model_name='mysearch',
            name='img',
            field=models.ImageField(blank=True, upload_to='./img'),
        ),
    ]
