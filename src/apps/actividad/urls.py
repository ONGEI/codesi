from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('actividad.views',
    url(r'^eventos/$','eventos',name='actividad-eventos'),
    url(r'^noticias/$','notas',name='actividad-notas'),
    url(r'^noticia/(?P<nota>\d+)/.*/$','nota',name='actividad-nota'),
    #url(r'^(?P<categoria>\d+)/(?P<norma>\d+)/.*/$','datelle',name='normatividad-datelle'),
)
