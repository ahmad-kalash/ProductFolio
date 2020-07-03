# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

from django.contrib import admin

from .models import (
    Product,
    ProductArea,
    ProductColor,
    ProductOrigin,
    ProductType,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ['slug']


admin.site.register(ProductArea)
admin.site.register(ProductColor)
admin.site.register(ProductOrigin)
admin.site.register(ProductType)
