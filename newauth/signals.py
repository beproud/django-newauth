# :coding=utf-8:

from django.dispatch import Signal

#: user logged in signal
user_logged_in = Signal(providing_args=['request', 'user'])

#: user logged out signal
user_logged_out = Signal(providing_args=['request', 'user'])
