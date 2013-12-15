import urllib
from urllib import FancyURLopener
import feedparser

from django.db import models
from django.conf import settings
from django.core.files import File
from django.utils import timezone

class Manga(models.Model):
    """A manga title being tracked by MangaPi."""
    
    title = models.CharField(max_length=50)
    #The last time MangaPi checked for new chapters
    last_update = models.DateTimeField('Last Update', default=timezone.now())
    #The last chapter read by the user
    last_read = models.ForeignKey('NewChapter', related_name='+', blank=True, null=True, default=None)
    #title in onemanga's url format, used to get to the RSS url
    title_url = models.CharField(max_length=50, null=True, default=None)
    #Saves image from onemanga for this manga
    image = models.ImageField(upload_to='manga_images/', null=True, default=None)
    
    def __init__(self, *args, **kwargs):
        """After calling django.db.models.Model.__init__(), calls Manga.updateImage()."""
        
        super(Manga, self).__init__(*args, **kwargs)
        self.updateImage();
        
    def __unicode__(self):
        return self.title
        
    def updateImage(self):
        """Connects to the manga's RSS feed and downloads it's image, saving to self.image."""
        
        filename = '{}manga_images/{}.jpg'.format(settings.MEDIA_ROOT, self.title_url)
        feed = feedparser.parse('http://www.onemanga.me/manga-rss/{}/'.format(self.title_url))
        img = ImageOpener().retrieve(feed.feed.image.href.replace('_32', '_200'), filename)
        self.image = filename
        
class NewChapter(models.Model):
    """A new chapter for a manga tracked by MangaPi."""
    
    link = models.URLField()
    manga = models.ForeignKey('Manga')
    found_time = models.DateTimeField('Found Time', default=timezone.now(), auto_now_add=True)
    
    def __unicode__(self):
        return 'New {}: {}'.format(self.manga.title, self.link)

class ImageOpener(FancyURLopener):
    """Spoofs Mozilla's identification to allow this bot to download from oneamanga.me."""
    
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'