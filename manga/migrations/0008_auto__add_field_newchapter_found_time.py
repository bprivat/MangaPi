# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewChapter.found_time'
        db.add_column(u'manga_newchapter', 'found_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 12, 14, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewChapter.found_time'
        db.delete_column(u'manga_newchapter', 'found_time')


    models = {
        u'manga.manga': {
            'Meta': {'object_name': 'Manga'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'last_read': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['manga.NewChapter']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 12, 14, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title_url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True'})
        },
        u'manga.newchapter': {
            'Meta': {'object_name': 'NewChapter'},
            'found_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 12, 14, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'manga': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manga.Manga']"})
        }
    }

    complete_apps = ['manga']