# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field tools on 'Plugin'
        db.create_table(u'plugin_plugin_tools', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('plugin', models.ForeignKey(orm[u'plugin.plugin'], null=False)),
            ('tool', models.ForeignKey(orm[u'tool.tool'], null=False))
        ))
        db.create_unique(u'plugin_plugin_tools', ['plugin_id', 'tool_id'])


    def backwards(self, orm):
        # Removing M2M table for field tools on 'Plugin'
        db.delete_table('plugin_plugin_tools')


    models = {
        u'plugin.plugin': {
            'Meta': {'object_name': 'Plugin'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tool.Tool']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'})
        },
        u'tool.tool': {
            'Meta': {'object_name': 'Tool'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['plugin']