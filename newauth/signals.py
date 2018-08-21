# :coding=utf-8:

from django.dispatch import Signal


#: This is `django.dispatch.Signal` instances, Notification send after a logged in.
#:
#: If you don't know `django.dispatch.Signal` see: https://docs.djangoproject.com/ja/1.11/topics/signals/
user_logged_in = Signal(providing_args=['request', 'user'])


#: This is `django.dispatch.Signal` instances. Notification send after a logged out.
#:
#: If you don't know `django.dispatch.Signal` see: https://docs.djangoproject.com/ja/1.11/topics/signals/
user_logged_out = Signal(providing_args=['request', 'user'])
