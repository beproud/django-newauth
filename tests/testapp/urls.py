#:coding=utf-8:
from django.urls import re_path, include
from django.http import HttpResponse

from newauth.decorators import login_required


def testview(request):
    return HttpResponse("Spam and Eggs")


urlpatterns = [
    re_path(r'^account/', include('newauth.urls')),
    re_path(r'^testapp/login_required/', login_required(testview)),
    re_path(r'^testapp/testapp_login_required', login_required(["testapp"])(testview)),
]
