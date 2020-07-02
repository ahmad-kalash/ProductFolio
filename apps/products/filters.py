# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

from django_filters import FilterSet

from .models import Product


class ProductFilter(FilterSet):

    class Meta:
        model = Product
        exclude = ['slug', 'description', 'image', 'old_price', 'updated_at', 'created_at']
