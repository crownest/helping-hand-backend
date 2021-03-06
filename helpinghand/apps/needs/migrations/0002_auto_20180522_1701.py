# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-22 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('needs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('is_fixed', models.BooleanField(default=False, verbose_name='Is Fixed')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='need_items', to='needs.Need', verbose_name='Need')),
            ],
            options={
                'verbose_name': 'Need Item',
                'verbose_name_plural': 'Need Items',
            },
        ),
        migrations.AlterUniqueTogether(
            name='needitem',
            unique_together=set([('name', 'need')]),
        ),
    ]
