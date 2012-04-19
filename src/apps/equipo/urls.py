from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('equipo.views',
    url(r'^(?P<equipo>\d+)/listar/$','listar',name='equipo-listar'),
    #url(r'^(?P<categoria>\d+)/(?P<norma>\d+)/.*/$','datelle',name='normatividad-datelle'),
)
