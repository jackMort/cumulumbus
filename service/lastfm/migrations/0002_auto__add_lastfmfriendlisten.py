# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LastfmFriendListen'
        db.create_table('lastfm_lastfmfriendlisten', (
            ('post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Post'], unique=True, primary_key=True)),
            ('friend', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('track', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('lastfm', ['LastfmFriendListen'])


    def backwards(self, orm):
        
        # Deleting model 'LastfmFriendListen'
        db.delete_table('lastfm_lastfmfriendlisten')


    models = {
        'core.post': {
            'Meta': {'object_name': 'Post'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ServiceAccount']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'readed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
        'lastfm.lastfmfriendlisten': {
            'Meta': {'object_name': 'LastfmFriendListen', '_ormbases': ['core.Post']},
            'friend': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'lastfm.lastfmpost': {
            'Meta': {'object_name': 'LastfmPost', '_ormbases': ['core.Post']},
            'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['lastfm']
