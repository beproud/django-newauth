# -*- coding: utf-8 -*-
try:
    from django.db.transaction import atomic
except ImportError:
    from django.db.transaction import commit_on_success as atomic

try:
    from django.contrib.admin.utils import flatten_fieldsets  # Django-1.7 or later
except ImportError:
    from django.contrib.admin.util import flatten_fieldsets

try:
    from django.utils.lru_cache import lru_cache  # Django-1.7 or later
    def memoize(func, cache, num_args):
        return lru_cache()(func)
except ImportError:
    from django.utils.functional import memoize
