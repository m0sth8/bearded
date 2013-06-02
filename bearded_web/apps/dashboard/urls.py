# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url



urlpatterns = patterns('dashboard.views',
    url('^target/$', 'target', name='target'),
    url('^job/$', 'job', name='job'),
    url('^template/.*$', 'template', name='template'),
    url('^report/$', 'report', name='report'),
    url('^vulnexplorer/$', 'vuln_explorer', name='vuln_explorer'),
    url('^$', 'target'),

)