# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-01 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compresult',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
