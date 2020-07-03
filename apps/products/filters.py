# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

from django import forms

from django_filters import (
    CharFilter,
    ChoiceFilter,
    FilterSet,
    ModelMultipleChoiceFilter,
    RangeFilter
)

from django_filters.widgets import RangeWidget

from .models import (
    models,
    Product,
    ProductOrigin,
    ProductType,
    ProductArea,
    ProductColor,
)


class CustomRangeWidget(RangeWidget):
    def __init__(self, min_value=None, max_value=None, attrs=None):
        super().__init__(attrs)
        if min_value:
            self.widgets[0].attrs.update(min_value)
        if max_value:
            self.widgets[1].attrs.update(max_value)


class ProductFilter(FilterSet):

    CHOICES = (
        ('descending', 'Descending'),
        ('ascending', 'Ascending'),
        ('price_low_high', 'Price: Low to High'),
        ('price_high_low', 'Price: High to Low'),
    )

    search = CharFilter(field_name='name', label='Name', lookup_expr='icontains')

    price = RangeFilter(
        field_name='price',
        widget=CustomRangeWidget(
            min_value={
                'value': '30',
                'placeholder': 'Min Price',
            },
            max_value={
                'value': '120',
                'placeholder': 'Max Price',
            },
            attrs={
                # 'type', 'range',
                'min': '30',
                'max': '120',
                # 'readonly': 'true',
            }
        )
    )

    origin = ModelMultipleChoiceFilter(
        queryset=ProductOrigin.objects.annotate(total_num=models.Count('product')).filter(total_num__gt=0),
        widget=forms.CheckboxSelectMultiple,
    )

    type = ModelMultipleChoiceFilter(
        queryset=ProductType.objects.annotate(total_num=models.Count('product')).filter(total_num__gt=0),
        widget=forms.CheckboxSelectMultiple,
    )

    area = ModelMultipleChoiceFilter(
        queryset=ProductArea.objects.annotate(total_num=models.Count('product')).filter(total_num__gt=0),
        widget=forms.CheckboxSelectMultiple,
    )

    color = ModelMultipleChoiceFilter(
        queryset=ProductColor.objects.annotate(total_num=models.Count('product')).filter(total_num__gt=0),
        widget=forms.CheckboxSelectMultiple,
    )

    ordering = ChoiceFilter(label='Sort By', choices=CHOICES, method='filter_by_order')


    class Meta:
        model = Product
        exclude = ['slug', 'description', 'image', 'old_price', 'updated_at', 'created_at']


    def filter_by_order(self, queryset, name, value):

        if value == 'ascending':
            expression = 'created_at'
        elif value == 'price_low_high':
            expression = 'price'
        elif value == 'price_high_low':
            expression = '-price'
        else:
            expression = '-created_at'

        return queryset.order_by(expression)


# Resources:
# Source1: https://github.com/Hopetree/izone/blob/master/apps/blog/templatetags/blog_tags.py
# Source2: https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
# Source3: https://etuannv.com/en/django-set-different-placeholders-for-rangefilter-or-datefromtorangefilter
# Source4: https://www.youtube.com/watch?v=nle3u6Ww6Xk
