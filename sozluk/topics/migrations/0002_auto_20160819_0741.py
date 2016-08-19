# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-19 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('created_at',), 'verbose_name': 'Baslik', 'verbose_name_plural': 'Basliklar'},
        ),
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ManyToManyField(blank=True, to='topics.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=140, unique=True, verbose_name='Title'),
        ),
    ]