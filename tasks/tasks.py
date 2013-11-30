from celery import task
from manga.models import Manga, NewChapter
import feedparser
from time import mktime
import datetime

@task()
def updateManga():
    for m in Manga.objects.all():
        doc = feedparser.parse('http://www.onemanga.me/manga-rss/{}'.format(m.title_url))
        latest = datetime.date.min
        for entry in doc.entries:
            if m.latest.timetuple() >= entry.published_parsed:
                break
            if latest.timetuple < entry.published_parsed:
                latest = datetime.fromtimestamp(mktime(entry.published_parsed))
                
            chapter = NewChapter(link=entry.links[0].href, manga=m)
            chapter.save()
        if m.latest < latest:
            m.latest = latest