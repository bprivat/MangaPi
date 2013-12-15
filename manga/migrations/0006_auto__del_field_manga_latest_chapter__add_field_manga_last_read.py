# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Manga.latest_chapter'
        db.delete_column(u'manga_manga', 'latest_chapter_id')

        # Adding field 'Manga.last_read'
        db.add_column(u'manga_manga', 'last_read',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['manga.NewChapter']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Manga.latest_chapter'
        db.add_column(u'manga_manga', 'latest_chapter',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, to=orm['manga.NewChapter'], blank=True),
                      keep_default=False)

        # Deleting field 'Manga.last_read'
        db.delete_column(u'manga_manga', 'last_read_id')


    models = {
        u'manga.manga': {
            'Meta': {'object_name': 'Manga'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'last_read': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['manga.NewChapter']"}),
            'last_update': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 12, 14, 0, 0)'}),
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