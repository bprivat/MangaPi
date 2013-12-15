import feedparser
import datetime
import urllib

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import generic

from manga.models import Manga, NewChapter

class UpdatesView(generic.ListView):
    """Shows any new updates to manga the user follows."""
    
    template_name = 'manga/updates.html'
    context_object_name = 'update_list'
    
    def get_queryset(self):
        return NewChapter.objects.order_by('-found_time')
        
class MangaDetailView(generic.DetailView):
    """Shows specific Manga details."""
    model = Manga
    template_name = 'manga/detail.html'
    
class TitlesView(generic.ListView):
    """Shows list of manga tracked by MangaPi."""
    
    template_name = 'manga/titles.html'
    context_object_name = 'manga_list'
    
    def get_queryset(self):
        return Manga.objects.order_by('title')
    
def add_manga(request):
    """Renders add.html form to add a new manga."""
    
    return render(request, 'manga/add.html')
    
def handle_add(request):
    """Called by add_manga form. Attempts to add a new manga with the given info."""
    
    if request.POST['url'] != '':
        #Take the last bit of the url, which is the url for this title
        title_url = request.POST['url'].rsplit('/', 2)[1]
        #The human readable title should be this url without '-' and '_'
        title = title_url.replace('-', ' ').replace('_', ' ').title()
        
        m = Manga(title=title, title_url=title_url, last_update=datetime.date.today())
        m.save()
        
    elif request.POST['title'] != '':
        return render(request, 'manga/add.html', {'error_msg': "Title not yet supported."})
    else:
        return render(request, 'manga/add.html', {'error_msg': "Must provide at least one field."})
        
    return redirect('manga:titles')
