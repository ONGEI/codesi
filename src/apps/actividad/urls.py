from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('actividad.views',
    url(r'^eventos/$','eventos',name='actividad-eventos'),
    url(r'^eventos/(?P<date_year>\d+)/$','eventos',name='actividad-eventos'),
    url(r'^noticias/$','noticias',name='actividad-notas'),
    url(r'^noticias/(?P<date_year>\d+)/$','noticias',name='actividad-notas'),
    url(r'^noticia/(?P<noticia>\d+)/.*/$','noticia',name='actividad-nota'),
    url(r'^informes/$','informes',name='actividad-informes'),
    url(r'^informes/(?P<date_year>\d+)/$','informes',name='actividad-informes'),
    url(r'^informe/(?P<informe>\d+)/.*/$','informe',name='actividad-informe'),
)
