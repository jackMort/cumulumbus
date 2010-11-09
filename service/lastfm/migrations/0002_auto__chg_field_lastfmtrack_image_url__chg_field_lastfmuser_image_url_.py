# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'LastfmTrack.image_url'
        db.alter_column('lastfm_lastfmtrack', 'image_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'LastfmUser.image_url'
        db.alter_column('lastfm_lastfmuser', 'image_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'LastfmArtist.image_url'
        db.alter_column('lastfm_lastfmartist', 'image_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'LastfmTrack.image_url'
        db.alter_column('lastfm_lastfmtrack', 'image_url', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'LastfmUser.image_url'
        db.alter_column('lastfm_lastfmuser', 'image_url', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'LastfmArtist.image_url'
        db.alter_column('lastfm_lastfmartist', 'image_url', self.gf('django.db.models.fields.CharField')(max_length=255))


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
        'lastfm.lastfmaccount': {
            'Meta': {'object_name': 'LastfmAccount', '_ormbases': ['core.ServiceAccount']},
            'serviceaccount_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.ServiceAccount']", 'unique': 'True', 'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lastfm.lastfmartist': {
            'Meta': {'object_name': 'LastfmArtist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'lastfm.lastfmfriendlisten': {
            'Meta': {'object_name': 'LastfmFriendListen', '_ormbases': ['core.Post']},
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lastfm.LastfmUser']"}),
            'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lastfm.LastfmTrack']"})
        },
        'lastfm.lastfmtrack': {
            'Meta': {'object_name': 'LastfmTrack'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lastfm.LastfmArtist']"}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'streamable': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'lastfm.lastfmuser': {
            'Meta': {'object_name': 'LastfmUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lastfm']
