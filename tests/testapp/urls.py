#:coding=utf-8:
from django.urls import path, include
from django.http import HttpResponse
from newauth.decorators import login_required


def testview(request):
    return HttpResponse("Spam and Eggs")


urlpatterns = [
    path('account/', include('newauth.urls')),
    path('testapp/login_required/', login_required(testview)),
    path('testapp/testapp_login_required', login_required(["testapp"])(testview)),
]
