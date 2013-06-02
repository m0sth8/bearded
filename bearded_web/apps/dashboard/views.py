# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils.translation import gettext as _

from plugin.models import Plugin
from plugin.api import PluginResource

DASHBOARD_MENUS = (
    {'url': reverse_lazy('dashboard:target'), 'appName': 'targetApp', 'title': _(u'Targets')},
    {'url': reverse_lazy('dashboard:template'), 'appName': 'templateApp', 'title': _(u'Templates')},
    {'url': reverse_lazy('dashboard:job'), 'appName': 'jobApp', 'title': _(u'Jobs')},
    {'url': reverse_lazy('dashboard:report'), 'appName': 'reportApp', 'title': _(u'Reports')},
    {'url': reverse_lazy('dashboard:vuln_explorer'), 'appName': 'vulnApp', 'title': _(u'Vuln explorer')},
)


@login_required
def target(request):
    ctx = {'dashboard_menus': DASHBOARD_MENUS}
    return render(request, 'dashboard/target.html', ctx)

@login_required
def template(request):
    plugin_resource = PluginResource()
    plugins = Plugin.objects.all()
    plugin_bundles = [plugin_resource.full_dehydrate(plugin_resource.build_bundle(obj=plugin)) for plugin in plugins]
    plugins_serialized = plugin_resource.serialize(None, plugin_bundles, 'application/json')
    ctx = {
        'dashboard_menus': DASHBOARD_MENUS,
        'tool_plugins': plugins_serialized,
    }
    return render(request, 'dashboard/template.html', ctx)

@login_required
def job(request):
    ctx = {'dashboard_menus': DASHBOARD_MENUS}
    return render(request, 'dashboard/job.html', ctx)

@login_required
def report(request):
    ctx = {'dashboard_menus': DASHBOARD_MENUS}
    return render(request, 'dashboard/report.html', ctx)

@login_required
def vuln_explorer(request):
    ctx = {'dashboard_menus': DASHBOARD_MENUS}
    return render(request, 'dashboard/vuln_explorer.html', ctx)