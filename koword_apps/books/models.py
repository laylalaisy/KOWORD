# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.db.models import Q

from users.models import UserProfile

class List(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    name = models.CharField(blank=True, max_length=200, verbose_name="name")
    unit = models.IntegerField(verbose_name='unit')
    author = models.CharField(blank=True, max_length=200, verbose_name="author")
    info = models.CharField(blank=True, max_length=200, verbose_name="info")

    class Meta:
        verbose_name = "books_list"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.info
