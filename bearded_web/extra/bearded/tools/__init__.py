# -*- coding: utf-8 -*-

import importlib

TOOLS = {
    # 'cli': 'bearded.tools.cl.CommandLineTool',
    'wpscan': 'bearded.tools.wpscan.WpScanTool',
    'nmap': 'bearded.tools.nmap.NmapTool',
}


def get_tool_class(name):
    tool_path = TOOLS.get(name)
    if not tool_path:
        return None
    tool_split_path = tool_path.split('.')
    tool_module_path, tool_class_name = '.'.join(tool_split_path[:-1]), tool_split_path[-1]
    tool_module = importlib.import_module(tool_module_path)
    ToolClass = getattr(tool_module, tool_class_name)
    return ToolClass


class BaseTool(object):
    name = None
    icon = None
    description = None

    @classmethod
    def get_name(cls):
        return cls.name if cls.name else cls.name
