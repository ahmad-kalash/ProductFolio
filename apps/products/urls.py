# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: MIT

from django.urls import path

from .views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
]
