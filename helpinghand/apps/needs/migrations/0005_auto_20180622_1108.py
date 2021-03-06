# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-22 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needs', '0004_auto_20180622_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='needitem',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='needitem',
            name='long',
        ),
        migrations.AddField(
            model_name='need',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=51.90949, max_digits=9, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='need',
            name='long',
            field=models.DecimalField(decimal_places=6, default=6.384903, max_digits=9, verbose_name='Longitude'),
        ),
    ]
