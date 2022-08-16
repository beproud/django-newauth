#:coding=utf-8:

from django.urls import path

from newauth.views import login, logout


urlpatterns = [
    path('login/', login, name='newauth_login'),
    path('logout/', logout, name='newauth_logout'),
]
