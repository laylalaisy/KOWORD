# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.db.models import Q

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
        return self.word


class Record(models.Model):
    userid = models.IntegerField(blank=True, verbose_name="userid")
    bookid = models.IntegerField(blank=True, verbose_name="bookid")
    unit = models.IntegerField(blank=True, verbose_name="unit")
    isfinished = models.IntegerField(verbose_name="isfinished", default=0)

    class Meta:
        verbose_name = "learn_record"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.id
