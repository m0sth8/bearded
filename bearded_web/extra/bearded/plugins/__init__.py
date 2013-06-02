# -*- coding: utf-8 -*-

import importlib

PLUGINS = {
    'parallel_sequence': 'bearded.plugins.sequence.ParallelSequencePlugin',
    'serial_sequence': 'bearded.plugins.sequence.SerialSequencePlugin',
    'cl': 'bearded.plugins.cl.CommandLineToolPlugin',
}


def get_plugin_class(name):
    plugin_path = PLUGINS.get(name)
    if not plugin_path:
        return None
    plugin_split_path = plugin_path.split('.')
    plugin_module_path, plugin_class_name = '.'.join(plugin_split_path[:-1]), plugin_split_path[-1]
    plugin_module = importlib.import_module(plugin_module_path)
    PluginClass = getattr(plugin_module, plugin_class_name)
    return PluginClass


class BasePlugin(object):
    description = None