#:coding=utf-8:

try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url

urlpatterns = patterns('newauth.views',
    url(r'^login/$', 'login', name='newauth_login'),
    url(r'^logout/$', 'logout', name='newauth_logout'),
)
