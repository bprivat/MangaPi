from datetime import date
import urllib
from urllib import FancyURLopener
import feedparser

from django.db import models
from django.conf import settings
from django.core.files import File

class Manga(models.Model):
    title = models.CharField(max_length=50)
    last_update = models.DateField('Last Update', default=date.today())
    latest = models.ForeignKey('NewChapter', related_name='+', null=True, default=None)
    
    title_url = models.CharField(max_length=50, null=True, default=None)
    image = models.ImageField(upload_to='manga_images/', null=True, default=None)
    
    def __unicode__(self):
        return self.title
        
    def updateImage(self):
        filename = '{}manga_images/{}.jpg'.format(settings.MEDIA_ROOT, self.title_url)
        feed = feedparser.parse('http://www.onemanga.me/manga-rss/{}/'.format(self.title_url))
        img = ImageOpener().retrieve(feed.feed.image.href.replace('_32', '_200'), filename)
        self.image = filename
        self.save()
        
class NewChapter(models.Model):
    link = models.URLField()
    manga = models.ForeignKey('Manga')
    
    def __unicode__(self):
        return 'New {}: {}'.format(self.manga.title, self.link)

class ImageOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'