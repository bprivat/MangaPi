# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manga'
        db.create_table(u'manga_manga', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title_url', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True)),
        ))
        db.send_create_signal(u'manga', ['Manga'])

        # Adding model 'NewChapter'
        db.create_table(u'manga_newchapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('manga', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['manga.Manga'])),
        ))
        db.send_create_signal(u'manga', ['NewChapter'])


    def backwards(self, orm):
        # Deleting model 'Manga'
        db.delete_table(u'manga_manga')

        # Deleting model 'NewChapter'
        db.delete_table(u'manga_newchapter')


    models = {
        u'manga.manga': {
            'Meta': {'object_name': 'Manga'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title_url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True'})
        },
        u'manga.newchapter': {
            'Meta': {'object_name': 'NewChapter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'manga': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manga.Manga']"})
        }
    }

    complete_apps = ['manga']