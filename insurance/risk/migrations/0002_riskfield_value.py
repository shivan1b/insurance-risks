# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-11 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskfield',
            name='value',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]