# -*- coding: utf-8 -*-

from django.contrib import admin

from template.models import Template


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'config', 'user', 'is_root', )
    list_filter = ('is_root', )
    date_hierarchy = 'created'
    raw_id_fields = ('user', 'sequence', )


admin.site.register(Template, TemplateAdmin)



