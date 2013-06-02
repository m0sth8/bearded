# -*- coding: utf-8 -*-

from django.db import models
from bearded.tools import get_tool_class


class Tool(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def _get_tool_class(self):
        return get_tool_class(self.name)

