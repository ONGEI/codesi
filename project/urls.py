# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve
from filebrowser.sites import site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    # Uncomment the next line to enable the admin:
    (r'^admin/projectadmin/',include('projectadmin.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    #app urls
    (r'^miembro/', include('miembro.urls')),
    (r'^normatividad/', include('normatividad.urls')),
    (r'^actividad/', include('actividad.urls')),
    (r'^equipo/', include('equipo.urls')),
    (r'^objetivo/', include('objetivo.urls')),
    url(r'^$', 'home.views.index'),
)

#if settings.DEBUG:
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$',
        serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^static/(?P<path>.*)$',
        serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$',
        'django.views.generic.simple.redirect_to',
        {'url': '/static/imagen/favicon.ico'}),
)
