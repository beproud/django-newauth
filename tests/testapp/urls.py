#:coding=utf-8:
from django.urls import path, include
from django.http import HttpResponse
from newauth import views
from newauth.decorators import login_required


def testview(request):
    return HttpResponse("Spam and Eggs")


urlpatterns = [
    path('account/login/', views.login, name='newauth_login'),
    path('account/logout/', views.logout, name='newauth_logout'),
    path('testapp/login_required/', login_required(testview), name='login_required'),
    path('testapp/testapp_login_required/', login_required(["testapp"])(testview), name='testapp_login_required'),
]
