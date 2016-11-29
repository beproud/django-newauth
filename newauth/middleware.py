#:coding=utf-8:

from django import VERSION as DJANGO_VERSION
from django.conf import settings

if DJANGO_VERSION >= (1, 10):
    from django.utils.deprecation import MiddlewareMixin
else:
    MiddlewareMixin = object

from newauth.constants import DEFAULT_USER_PROPERTY


class LazyUser(object):
    """
    Lazily creates the user object.
    """
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_newauth_cached_user'):
            from newauth.api import get_user_from_request
            request._newauth_cached_user = get_user_from_request(request)
        return request._newauth_cached_user


class AuthMiddleware(MiddlewareMixin):
    """
    Middleware for getting the current user object
    and attaching it to the request.
    """
    def process_request(self, request):
        user_prop = getattr(settings, 'NEWAUTH_USER_PROPERTY', DEFAULT_USER_PROPERTY)
        setattr(request.__class__, user_prop, LazyUser())
        return None
