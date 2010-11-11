# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TwitterAccount'
        db.create_table('twitter_twitteraccount', (
            ('serviceaccount_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.ServiceAccount'], unique=True, primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('twitter', ['TwitterAccount'])

        # Adding model 'TwitterUser'
        db.create_table('twitter_twitteruser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('twitter', ['TwitterUser'])

        # Adding model 'TwitterPost'
        db.create_table('twitter_twitterpost', (
            ('post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Post'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['twitter.TwitterUser'])),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('twitter', ['TwitterPost'])


    def backwards(self, orm):
        
        # Deleting model 'TwitterAccount'
        db.delete_table('twitter_twitteraccount')

        # Deleting model 'TwitterUser'
        db.delete_table('twitter_twitteruser')

        # Deleting model 'TwitterPost'
        db.delete_table('twitter_twitterpost')


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
        'twitter.twitteraccount': {
            'Meta': {'object_name': 'TwitterAccount', '_ormbases': ['core.ServiceAccount']},
            'serviceaccount_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.ServiceAccount']", 'unique': 'True', 'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'twitter.twitterpost': {
            'Meta': {'object_name': 'TwitterPost', '_ormbases': ['core.Post']},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['twitter.TwitterUser']"})
        },
        'twitter.twitteruser': {
            'Meta': {'object_name': 'TwitterUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['twitter']
