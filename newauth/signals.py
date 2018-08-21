# :coding=utf-8:

from django.dispatch import Signal


user_logged_in = Signal(providing_args=['request', 'user'])
"""
This is `django.dispatch.Signal` instances.
This is sent at the end of the `newauth.api.login()` method.

Arguments sent with this signal:

**sender**

    The class of the user that just logged in.

**request**

    The current `django.http.request.HttpRequest` instance.

**user**

    The user instance that just logged in.
"""


user_logged_out = Signal(providing_args=['request', 'user'])
"""
This is `django.dispatch.Signal` instances.
This is sent at the end of the `newauth.api.logout()` method.

Arguments sent with this signal:

**sender**

    As above: the class of the user that just logged out or None if the user was not authenticated.

**request**

    The current `django.http.request.HttpRequest` instance.

**user**

    The user instance that just logged out or None if the user was not authenticated.
"""
