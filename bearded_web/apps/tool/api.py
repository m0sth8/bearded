# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication

from tool.models import Tool
from bearded_web.core.api.serializer import CamelCaseJSONSerializer
from bearded_web.core.api.authorization import UserObjectsOnlyAuthorization


class ToolResource(ModelResource):
    class Meta:
        queryset = Tool.objects.filter(available=True)
        # authentication = SessionAuthentication()
        # authorization = UserObjectsOnlyAuthorization()
        serializer = CamelCaseJSONSerializer()
