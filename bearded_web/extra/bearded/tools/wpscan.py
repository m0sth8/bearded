# -*- coding: utf-8 -*-
# from gevent.subprocess import


from bearded.tools.cl import CommandLineTool


class WpScanTool(CommandLineTool):

    def __init__(self):
        super(WpScanTool, self).__init__()

    def _get_command_name(self):
        return '/home/vagrant/tools/wpscan/wpscan.rb'

    def get_version(self):
        return '123'


