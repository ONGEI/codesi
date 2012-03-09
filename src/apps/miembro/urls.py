from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('miembro.views',
    url(r'^listar/$','listar',name='miembro-listar|'),
    #url(r'^(?P<post_id>\d+)/register/comment/$','register_comment',name='pecert-post-register-comment'),
    #url(r'^search/$','search_post',name='pecert-post-search'),
)
