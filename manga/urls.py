from django.conf.urls import patterns, url

from manga import views, startup

urlpatterns = patterns('',
    url(r'^$', views.UpdatesView.as_view(), name='updates'),
    url(r'^titles/$', views.TitlesView.as_view(), name='titles'),
    url(r'^titles/(?P<pk>\d+)/$', views.MangaDetailView.as_view(), name='manga_detail'),
    url(r'^add/$', views.add_manga, name='add_manga'),
    url(r'^handle_add/$', views.handle_add, name='handle_add')
)

#Hacky startup location
#Should run once on startup
startup()