# -*- coding: utf-8 -*-

from django.contrib import admin

from target.models import Target


class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'user', )
    date_hierarchy = 'created'
    raw_id_fields = ('user', )


admin.site.register(Target, TargetAdmin)



