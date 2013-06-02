# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource, fields
from tastypie.authentication import SessionAuthentication

from template.models import Template
from bearded_web.core.api.serializer import CamelCaseJSONSerializer
from bearded_web.core.api.authorization import UserObjectsOnlyAuthorization


class TemplateResource(ModelResource):
    plugin = fields.ForeignKey('plugin.api.PluginResource', 'plugin')
    sequence = fields.ManyToManyField('template.api.TemplateResource', 'sequence')

    class Meta:
        queryset = Template.objects.all()
        authentication = SessionAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        serializer = CamelCaseJSONSerializer()
        filtering = {
            'is_root': ('exact', )
        }
