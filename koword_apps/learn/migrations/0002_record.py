# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-30 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False, verbose_name='id')),
                ('userid', models.IntegerField(blank=True, verbose_name='userid')),
                ('bookid', models.IntegerField(blank=True, verbose_name='bookid')),
                ('unit', models.IntegerField(blank=True, verbose_name='unit')),
                ('isfinished', models.IntegerField(blank=True, verbose_name='isfinished')),
            ],
            options={
                'verbose_name_plural': 'learn_record',
                'verbose_name': 'learn_record',
            },
        ),
    ]
