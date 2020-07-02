# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

from django import forms

from django_filters import FilterSet, ModelMultipleChoiceFilter

from .models import (
    models,
    Product,
    ProductOrigin,
    ProductType,
    ProductArea,
    ProductColor,
)

class ProductFilter(FilterSet):

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

    class Meta:
        model = Product
        exclude = ['slug', 'description', 'image', 'old_price', 'updated_at', 'created_at']


# Resources:
# Source1: https://github.com/Hopetree/izone/blob/master/apps/blog/templatetags/blog_tags.py
# Source2: https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
