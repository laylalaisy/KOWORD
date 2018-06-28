# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class UserProfile(AbstractUser):
    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.username

