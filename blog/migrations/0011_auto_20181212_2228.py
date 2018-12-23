# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-12-12 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_mysearch_created_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysearch',
            old_name='model_name',
            new_name='Class',
        ),
        migrations.AddField(
            model_name='mysearch',
            name='created_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mysearch',
            name='file',
            field=models.FileField(blank=True, upload_to='./file/'),
        ),
        migrations.AddField(
            model_name='mysearch',
            name='img',
            field=models.ImageField(blank=True, upload_to='/.img'),
        ),
        migrations.AddField(
            model_name='mysearch',
            name='publish_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='mysearch',
            name='content',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]