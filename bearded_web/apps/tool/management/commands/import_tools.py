# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from tool.models import Tool
# from bearded.tools import TOOLS, get_tool_class


class Command(BaseCommand):
    help = "Import existed tools"

    def update(self, tool, ToolClass):
        if ToolClass.icon:
            tool.icon = ToolClass.icon
        if ToolClass.description:
            tool.description = ToolClass.description
        tool.save()
        return tool

    def handle(self, *args, **options):
        tools_map = dict([(tool.name, tool, ) for tool in Tool.objects.filter(available=True)])
        for tool_name in TOOLS.iterkeys():
            ToolClass = get_tool_class(tool_name)
            if ToolClass:
                tool, created = Tool.objects.get_or_create(name=tool_name,
                                                           defaults={
                                                               'description': ToolClass.description,
                                                               # 'icon': ToolClass.icon,
                                                           })
                self.stdout.write('[{status}] {name}'.format(name=tool.name,
                                                             status=('+' if created else ' ')))
                if tool.name in tools_map:
                    tools_map.pop(tool.name)

        for tool in tools_map.itervalues():
            tool.available = False
            tool.save()
            self.stdout.write('[{status}] {name}'.format(name=tool.name,
                                                         status='-'))
