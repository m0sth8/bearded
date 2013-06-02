# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication

from servers.models import Server
from bearded_web.core.api.serializer import CamelCaseJSONSerializer
from bearded_web.core.api.authorization import UserObjectsOnlyAuthorization


class ServerResource(ModelResource):
    class Meta:
        queryset = Server.objects.all()
        authentication = SessionAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        serializer = CamelCaseJSONSerializer()

    def obj_delete_list(self, bundle, **kwargs):
        super(ServerResource, self).obj_delete_list(bundle, **kwargs)

