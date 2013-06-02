# -*- coding: utf-8 -*-

# sequence template
from plugin.models import Plugin


class BasePlugin(object):
    pass


class SerialSequencePlugin(BasePlugin):
    name = 'sequence.serial'
    description = u'Позволяет выполнять плагины последовательно'
    type = Plugin.PLUGIN_TYPE.SEQUENCE


class ParallelSequencePlugin(BasePlugin):
    name = 'sequence.parallel'
    description = u'Позволяет выполнять плагины параллельно'
    type = Plugin.PLUGIN_TYPE.SEQUENCE


class WpScanToolPlugin(BasePlugin):
    name = 'tool.wpscan'
    description = u'Сканирование при помощи wpScan'
    type = Plugin.PLUGIN_TYPE.TOOL