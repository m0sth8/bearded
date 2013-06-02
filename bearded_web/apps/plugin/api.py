# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource, fields
from tastypie.authentication import SessionAuthentication

from plugin.models import Plugin
from bearded_web.core.api.serializer import CamelCaseJSONSerializer
from bearded_web.core.api.authorization import UserObjectsOnlyAuthorization


class PluginResource(ModelResource):
    # tools = fields.ManyToManyField('tool.api.ToolResource', 'tools', null=True)

    class Meta:
        queryset = Plugin.objects.all()
        # authentication = SessionAuthentication()
        # authorization = UserObjectsOnlyAuthorization()
        serializer = CamelCaseJSONSerializer()
