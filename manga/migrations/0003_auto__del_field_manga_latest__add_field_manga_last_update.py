# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Manga.latest'
        db.delete_column(u'manga_manga', 'latest')

        # Adding field 'Manga.last_update'
        db.add_column(u'manga_manga', 'last_update',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 9, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Manga.latest'
        db.add_column(u'manga_manga', 'latest',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 9, 0, 0)),
                      keep_default=False)

        # Deleting field 'Manga.last_update'
        db.delete_column(u'manga_manga', 'last_update')


    models = {
        u'manga.manga': {
            'Meta': {'object_name': 'Manga'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 10, 9, 0, 0)'}),
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