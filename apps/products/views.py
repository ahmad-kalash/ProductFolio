# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

from django_filters.views import FilterView

from .filters import Product, ProductFilter


class ProductListView(FilterView):
    model = Product
    filterset_class = ProductFilter
    template_name = 'products/product_list.html'
    paginate_by = 1

    # TBD: solve pagination problem with filter
