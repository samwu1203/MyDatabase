# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-12-02 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mysearch',
            fields=[
                ('title', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('model_name', models.TextField(blank=True, null=True)),
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('created_data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]