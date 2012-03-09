from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('home.views',
    url(r'^(?P<post_id>\d+)/.*/$','show_post',name='pecert-show-post'),
    url(r'^(?P<post_id>\d+)/register/comment/$','register_comment',name='pecert-post-register-comment'),
    url(r'^search/$','search_post',name='pecert-post-search'),
)
