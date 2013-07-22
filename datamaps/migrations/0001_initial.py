# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'World'
        db.create_table(u'datamaps_world', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default='#EDDC4E', max_length=8)),
        ))
        db.send_create_signal(u'datamaps', ['World'])

        # Adding model 'Scope'
        db.create_table(u'datamaps_scope', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('topo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lon', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('scale', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=8)),
            ('color', self.gf('django.db.models.fields.CharField')(default='#EDDC4E', max_length=8)),
        ))
        db.send_create_signal(u'datamaps', ['Scope'])

        # Adding model 'Country'
        db.create_table(u'datamaps_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('scope', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datamaps.Scope'], null=True, blank=True)),
            ('topo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lon', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('radius', self.gf('django.db.models.fields.PositiveIntegerField')(default=10)),
            ('color', self.gf('django.db.models.fields.CharField')(default='#EDDC4E', max_length=8)),
        ))
        db.send_create_signal(u'datamaps', ['Country'])


    def backwards(self, orm):
        # Deleting model 'World'
        db.delete_table(u'datamaps_world')

        # Deleting model 'Scope'
        db.delete_table(u'datamaps_scope')

        # Deleting model 'Country'
        db.delete_table(u'datamaps_country')


    models = {
        u'datamaps.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#EDDC4E'", 'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#EDDC4E'", 'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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