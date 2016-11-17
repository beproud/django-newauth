#:coding=utf-8:
from django.conf.urls import patterns, include
from django.http import HttpResponse

from newauth.decorators import login_required

urlpatterns = patterns('',
    (r'^account/', include('newauth.urls')),
    (r'^testapp/login_required/', login_required(lambda request: HttpResponse("Spam and Eggs"))),
    (r'^testapp/testapp_login_required', login_required(["testapp"])(lambda request: HttpResponse("Spam and Eggs"))),
)
