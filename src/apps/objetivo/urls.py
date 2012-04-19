from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('objetivo.views',
    url(r'^(?P<objetivo>\d+)/describir/$','describir',name='objetivo-describir'),
    #url(r'^(?P<categoria>\d+)/(?P<norma>\d+)/.*/$','datelle',name='normatividad-datelle'),
)
