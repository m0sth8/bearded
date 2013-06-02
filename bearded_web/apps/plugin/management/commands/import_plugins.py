# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from plugin.models import Plugin, get_plugin_class
from bearded.plugins import PLUGINS


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        plugins_map = dict([(plugin.name, plugin, ) for plugin in Plugin.objects.filter(available=True)])
        for plugin_name in PLUGINS.iterkeys():
            PluginClass = get_plugin_class(plugin_name)
            if PluginClass:
                plugin, created = Plugin.objects.get_or_create(name=plugin_name,
                                                               defaults={
                                                                   'description': PluginClass.description,
                                                               })
                self.stdout.write('[{status}] {name}'.format(name=plugin.name,
                                                             status=('+' if created else ' ')))
                if plugin.name in plugins_map:
                    plugins_map.pop(plugin.name)

        for plugin in plugins_map.itervalues():
            plugin.available = False
            plugin.save()
            self.stdout.write('[{status}] {name}'.format(name=plugin.name,
                                                         status='-'))

