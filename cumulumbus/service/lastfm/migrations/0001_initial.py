# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LastfmAccount'
        db.create_table('lastfm_lastfmaccount', (
            ('serviceaccount_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.ServiceAccount'], unique=True, primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('lastfm', ['LastfmAccount'])

        # Adding model 'LastfmUser'
        db.create_table('lastfm_lastfmuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mbid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('lastfm', ['LastfmUser'])

        # Adding model 'LastfmArtist'
        db.create_table('lastfm_lastfmartist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mbid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('lastfm', ['LastfmArtist'])

        # Adding model 'LastfmTrack'
        db.create_table('lastfm_lastfmtrack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mbid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lastfm.LastfmArtist'])),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('streamable', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('lastfm', ['LastfmTrack'])

        # Adding model 'LastfmFriendListen'
        db.create_table('lastfm_lastfmfriendlisten', (
            ('post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Post'], unique=True, primary_key=True)),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lastfm.LastfmUser'])),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lastfm.LastfmTrack'])),
        ))
        db.send_create_signal('lastfm', ['LastfmFriendListen'])


    def backwards(self, orm):
        
        # Deleting model 'LastfmAccount'
        db.delete_table('lastfm_lastfmaccount')

        # Deleting model 'LastfmUser'
        db.delete_table('lastfm_lastfmuser')

        # Deleting model 'LastfmArtist'
        db.delete_table('lastfm_lastfmartist')

        # Deleting model 'LastfmTrack'
        db.delete_table('lastfm_lastfmtrack')

        # Deleting model 'LastfmFriendListen'
        db.delete_table('lastfm_lastfmfriendlisten')


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
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'streamable': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'lastfm.lastfmuser': {
            'Meta': {'object_name': 'LastfmUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lastfm']
