# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-29 01:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180628_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mobile_phone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nick_name',
        ),
    ]