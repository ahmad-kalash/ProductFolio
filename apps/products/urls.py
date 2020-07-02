# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

from django.urls import path

from .views import ProductListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list')
]
