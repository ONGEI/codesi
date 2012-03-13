from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('actividad.views',
    url(r'^eventos/$','eventos',name='actividad-eventos|'),
    #url(r'^(?P<categoria>\d+)/(?P<norma>\d+)/.*/$','datelle',name='normatividad-datelle'),
)
