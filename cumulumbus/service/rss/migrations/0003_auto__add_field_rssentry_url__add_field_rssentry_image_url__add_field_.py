# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'RSSEntry.url'
        db.add_column('rss_rssentry', 'url', self.gf('django.db.models.fields.URLField')(default=None, max_length=200), keep_default=False)

        # Adding field 'RSSEntry.image_url'
        db.add_column('rss_rssentry', 'image_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'RSSEntry.body'
        db.add_column('rss_rssentry', 'body', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'RSSEntry.url'
        db.delete_column('rss_rssentry', 'url')

        # Deleting field 'RSSEntry.image_url'
        db.delete_column('rss_rssentry', 'image_url')

        # Deleting field 'RSSEntry.body'
        db.delete_column('rss_rssentry', 'body')


    models = {
        'core.post': {
            'Meta': {'object_name': 'Post'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ServiceAccount']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'readed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'core.serviceaccount': {
            'Meta': {'object_name': 'ServiceAccount'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_import': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rss.rssaccount': {
            'Meta': {'object_name': 'RSSAccount', '_ormbases': ['core.ServiceAccount']},
            'serviceaccount_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.ServiceAccount']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'rss.rssentry': {
            'Meta': {'object_name': 'RSSEntry', '_ormbases': ['core.Post']},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['rss']
