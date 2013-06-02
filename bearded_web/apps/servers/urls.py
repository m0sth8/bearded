# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = patterns('servers.views',
    url(r'^(?P<server_id>\d+)/$', 'server', name='server'),
    url(r'^(?P<server_id>\d+)/scans/$', 'scans', name='scans'),
    url(r'^(?P<server_id>\d+)/scans/(?P<scan_id>\d+)/$', 'scan', name='scan'),
    url(r'^$',  'servers'),
    # url(r'^$', RedirectView.as_view(url=reverse_lazy('dashboard:servers'))),
)