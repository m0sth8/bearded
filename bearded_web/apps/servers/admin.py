# -*- coding: utf-8 -*-

from django.contrib import admin

from servers.models import Server, ScanTask


class ServerAdmin(admin.ModelAdmin):
    list_display = ('host', 'user', )
    date_hierarchy = 'created'
    raw_id_fields = ('user', )


class ScanTaskAdmin(admin.ModelAdmin):
    list_display = ('server', 'user', 'status', )
    date_hierarchy = 'created'
    list_filter = ('status', )
    raw_id_fields = ('user', 'server', )



admin.site.register(Server, ServerAdmin)
admin.site.register(ScanTask, ScanTaskAdmin)



