# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')

# Use this until https://github.com/jazzband/django-configurations/pull/251 is merged
from configurations import importer

importer.install()

try:
    from django.core.asgi import get_asgi_application
except ImportError:
    from django.core.handlers.asgi import ASGIHandler

    def get_asgi_application():
        return ASGIHandler()

application = get_asgi_application()
