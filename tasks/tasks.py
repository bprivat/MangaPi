from celery import task
from manga.models import Manga, NewChapter
import feedparser
from time import mktime, strptime
import datetime
from django.utils import timezone

@task()
def updateManga():
    """Connects to onemanga.me and checks for any chapters added after the manga was last checked."""
    
    for m in Manga.objects.all():
        doc = feedparser.parse('http://www.onemanga.me/manga-rss/{}'.format(m.title_url))
        for entry in doc.entries:
            #If the entry is in the past, all further entries will be, too. So, stop looking.
            if m.last_update.timetuple() >= strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z'):
                break
            
            #Otherwise, this chapter hasn't been looked at yet, so add it
            chapter = NewChapter(link=entry.links[0].href, manga=m)
            chapter.save()
        #We've now looked at all chapters for this manga, so update its date    
        m.last_update = timezone.now()
        m.save()