#:coding=utf-8:

from django.conf.urls import url

from newauth.views import login, logout


urlpatterns = [
    url(r'^login/$', login, name='newauth_login'),
    url(r'^logout/$', logout, name='newauth_logout'),
]
