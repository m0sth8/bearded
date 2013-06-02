# -*- coding: utf-8 -*-

from django.contrib import admin

from plugin.models import Plugin


class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'available', 'description', )

admin.site.register(Plugin, PluginAdmin)

