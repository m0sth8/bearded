# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import ModificationDateTimeField, CreationDateTimeField
from django_extensions.db.fields.json import JSONField


class Target(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(to=get_user_model())
    host = models.CharField(_('host'), max_length=255, help_text=_('domain or ip address'))
    created = CreationDateTimeField(_('Created'))
    modified = ModificationDateTimeField(_('Modified'))
    info = JSONField(null=True, blank=True)
    info_raw = models.TextField(null=True, blank=True)

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)

    def __unicode__(self):
        return u'%s[%s]' % (self.name, self.host, )
