from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import generic

from manga.models import Manga, NewChapter

import feedparser
import datetime
import urllib

class UpdatesView(generic.ListView):
    template_name = 'manga/updates.html'
    context_object_name = 'update_list'
    
    def get_queryset(self):
        return NewChapter.objects.order_by('-manga__latest')
        
class MangaDetailView(generic.DetailView):
    model = Manga
    template_name = 'manga/detail.html'
        
def titles(request):
    mangaList = Manga.objects.order_by('title')
    context = {'mangaList' : mangaList}
    return render(request, 'manga/titles.html', context)
    
def add_manga(request):
    return render(request, 'manga/add.html')
    
def handle_add(request):
    if request.POST['url'] != '':
        title_url = request.POST['url'].rsplit('/', 2)[1]
        title = title_url.replace('-', ' ').replace('_', ' ').title()
        
        m = Manga(title=title, title_url=title_url, latest=datetime.date.today())
        m.updateImage()
        m.save()
        
    elif request.POST['title'] != '':
        return render(request, 'manga/add.html', {'error_msg': "Title not yet supported."})
    else:
        return render(request, 'manga/add.html', {'error_msg': "Must provide at least one field."})
        
    return redirect('manga:titles')
