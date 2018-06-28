# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class UserProfile(AbstractUser):
    nick_name = models.CharField(blank=True,
                                 verbose_name=u"昵称",
                                 max_length=100)
    avatar = models.ImageField(upload_to="images/%Y/%m",
                               verbose_name=u"头像",
                               blank=True,
                               max_length=200)
    mobile_phone = models.CharField(blank=True,
                                    null=True,
                                    verbose_name=u"手机号",
                                    max_length=20)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def membership_days(self):
        delta = datetime.now() - self.date_joined
        return delta.days

    def unread_message_count(self):
        from operations.models import UserMessage
        return UserMessage.objects.filter(to_user=self.id, has_read=False).count()

    def unread_messages(self):
        from operations.models import UserMessage
        return UserMessage.objects.filter(to_user=self.id, has_read=False).all()

    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return static('AdminLTE/img/avatar2.png')

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        if self.nick_name:
            return self.nick_name
        return self.username
