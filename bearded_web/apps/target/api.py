# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication

from target.models import Target
from bearded_web.core.api.serializer import CamelCaseJSONSerializer
from bearded_web.core.api.authorization import UserObjectsOnlyAuthorization


class TargetResource(ModelResource):
    class Meta:
        queryset = Target.objects.all()
        authentication = SessionAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        serializer = CamelCaseJSONSerializer()
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        return super(TargetResource, self).obj_create(bundle, user=bundle.request.user)

