#:coding=utf-8:
from django.conf.urls import url, include
from django.http import HttpResponse

from newauth.decorators import login_required


def testview(request):
    return HttpResponse("Spam and Eggs")


urlpatterns = [
    url(r'^account/', include('newauth.urls')),
    url(r'^testapp/login_required/', login_required(testview)),
    url(r'^testapp/testapp_login_required', login_required(["testapp"])(testview)),
]
