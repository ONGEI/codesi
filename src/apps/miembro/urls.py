from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('miembro.views',
    url(r'^listar/$','listar',name='miembro-listar|'),
)
