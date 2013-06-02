# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import ModificationDateTimeField, CreationDateTimeField
from jsonfield import JSONField


class Template(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_root = models.BooleanField(default=True, db_index=True)
    plugin = models.ForeignKey(to='plugin.Plugin', null=True)
    config = JSONField(blank=True, null=True)
    user = models.ForeignKey(to=get_user_model(), related_name='+')
    created = CreationDateTimeField(_('Created'))
    modified = ModificationDateTimeField(_('Modified'))
    sequence = models.ManyToManyField(to='Template', null=True, blank=True)