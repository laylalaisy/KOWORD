# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.db.models import Q

from users.models import UserProfile

class Word(models.Model):
    id = models.IntegerField(blank=True, primary_key=True, verbose_name="id")
    bookname = models.CharField(blank=True, max_length=50, verbose_name="bookname")
    unit = models.IntegerField(verbose_name='unit')
    word = models.CharField(blank=True, max_length=50, verbose_name="word")
    meaning = models.CharField(blank=True, max_length=50, verbose_name="meaning")

    class Meta:
        verbose_name = "learn_word"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.info
