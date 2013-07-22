# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.color'
        db.add_column(u'datamaps_country', 'color',
                      self.gf('django.db.models.fields.CharField')(default='#EDDC4E', max_length=8),
                      keep_default=False)

        # Adding field 'Scope.color'
        db.add_column(u'datamaps_scope', 'color',
                      self.gf('django.db.models.fields.CharField')(default='#EDDC4E', max_length=8),
                      keep_default=False)

        # Adding field 'World.color'
        db.add_column(u'datamaps_world', 'color',
                      self.gf('django.db.models.fields.CharField')(default='#EDDC4E', max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.color'
        db.delete_column(u'datamaps_country', 'color')

        # Deleting field 'Scope.color'
        db.delete_column(u'datamaps_scope', 'color')

        # Deleting field 'World.color'
        db.delete_column(u'datamaps_world', 'color')


    models = {
        u'datamaps.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#EDDC4E'", 'max_length': '8'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'radius': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'scope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datamaps.Scope']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'topo': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'datamaps.scope': {
            'Meta': {'object_name': 'Scope'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#EDDC4E'", 'max_length': '8'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'scale': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '8'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'topo': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'datamaps.world': {
            'Meta': {'object_name': 'World'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#EDDC4E'", 'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topo': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['datamaps']