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
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

from django.core.asgi import get_asgi_application

application = get_asgi_application()
