.. release procedure

Procedure:

1. check CI status testing result: https://github.com/beproud/django-newauth/actions
2. update release version/date in ``ChangeLog.rst``
3. tagging version e.g. ``git tag 0.40``.
5. run ``python setup.py release sdist bdist_wheel``
6. upload ``twine upload dist/*``
7. check PyPI page: https://pypi.org/p/django-newauth
8. bump version in ``ChangeLog.rst`` and commit/push them onto GitHub
