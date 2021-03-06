# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-22 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needs', '0005_auto_20180622_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='need',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, verbose_name='Longitude'),
        ),
    ]
