from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

from bearded_web.api import v1_api


admin.autodiscover()

urlpatterns = patterns('',
       # system
       url(r'^admin/', include(admin.site.urls)),
       url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),

       # url(r'^servers/', include('servers.urls', namespace='servers')),


       # account
       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'},
           name='login'),
       url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

       url(r'^api/', include(v1_api.urls)),

       url(r'^$', 'bearded_web.views.index')
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()