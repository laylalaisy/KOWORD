# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-30 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_auto_20180630_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='isfinished',
            field=models.BooleanField(default=False, verbose_name='isfinished'),
        ),
    ]