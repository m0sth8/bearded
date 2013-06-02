# -*- coding: utf-8 -*-

from tastypie.api import Api

from target.api import TargetResource
from template.api import TemplateResource
from tool.api import ToolResource
from plugin.api import PluginResource


v1_api = Api(api_name='v1')
v1_api.register(TargetResource())
v1_api.register(TemplateResource())
v1_api.register(ToolResource())
v1_api.register(PluginResource())