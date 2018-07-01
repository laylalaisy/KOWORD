# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.db.models import Q

class Record(models.Model):
    userid = models.IntegerField(blank=True, verbose_name="userid")
    bookid = models.IntegerField(blank=True, verbose_name="bookid")
    unit = models.IntegerField(blank=True, verbose_name="unit")
    isexamed = models.IntegerField(verbose_name="isexamwed", default=0)
    examtime = models.DateTimeField(default=datetime.now, verbose_name="examtime")

    class Meta:
        verbose_name = "exam_record"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.id
