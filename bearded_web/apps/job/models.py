# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import ModificationDateTimeField, CreationDateTimeField
from jsonfield import JSONField

from bearded_web.core.fields import Choice


class Job(models.Model):
    class STATUS(Choice):
        CREATED = 1
        WORKS = 2  # обработка
        WAIT = 3  # ожидание ресурсов
        COMPLETED = 10

    # template =
    user = models.ForeignKey(to=get_user_model(), related_name='+')
    target = models.ForeignKey(to='target.Target')
    created = CreationDateTimeField(_('Created'))
    modified = ModificationDateTimeField(_('Modified'))

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)


class JobFrame(models.Model):
    class STATUS(Choice):
        CREATED = 1
        WORKS = 2  # обработка
        WAIT = 3  # ожидание ресурсов
        COMPLETED = 10

    job = models.ForeignKey(to='Job')
    parent = models.Parent(to='self', null=True, blank=True)
    user = models.ForeignKey(to=get_user_model(), related_name='+')

    # context = models.ForeignKey(to='FrameContext')

    created = CreationDateTimeField(_('Created'))
    modified = ModificationDateTimeField(_('Modified'))


# class FrameContext(models.Model):
#     data = JSONField()
