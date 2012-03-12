from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('normatividad.views',
    url(r'^(?P<categoria>\d+)/listar/$','listar',name='normatividad-listar|'),
    url(r'^(?P<categoria>\d+)/(?P<norma>\d+)/.*/$','datelle',name='normatividad-datelle'),
)
