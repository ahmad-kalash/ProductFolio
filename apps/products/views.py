# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

from django.views.generic import DetailView

from django_filters.views import FilterView

from .filters import Product, ProductFilter


class ProductListView(FilterView):
    model = Product
    filterset_class = ProductFilter
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            query_dect = self.request.GET.copy()
            # print(query_dect)
            if self.request.GET.get('page'):
                del query_dect['page']
                # print(query_dect)
            context['querystring'] = query_dect.urlencode()
            # print(query_dect.urlencode())
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


# Resources:
# Source1: https://stackoverflow.com/questions/51389848/how-can-i-use-pagination-with-django-filter
