# -*- coding: utf-8 -*-

from django.db import models

from bearded.plugins import get_plugin_class
from bearded_web.core.fields import Choice


class Plugin(models.Model):
    class PLUGIN_TYPE(Choice):
        SEQUENCE = 1
        TOOL = 3
        COMPOSITE = 5

    class STATUS(Choice):
        DISABLED = 1
        ENABLED = 2

    name = models.CharField(max_length=255, unique=True)
    type = models.PositiveSmallIntegerField(choices=PLUGIN_TYPE, default=PLUGIN_TYPE.TOOL)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    # tools = models.ManyToManyField(to='tool.Tool', blank=True, null=True)

    def __unicode__(self):
        return self.name

    def _get_plugin_class(self):
        return get_plugin_class(self.name)

