# -*- coding: utf-8 -*-

from django.contrib import admin

from tool.models import Tool


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Tool, ToolAdmin)