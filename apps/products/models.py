# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

from django.db import models
from django.urls import reverse_lazy


class ProductOrigin(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='eg: Spanish, Indian, Iraqi...')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
    

class ProductType(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='eg: Ceramic, Porsilan, Marmar...')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class ProductArea(models.Model):
    area = models.CharField(max_length=50, unique=True, help_text='eg: 24cm x 24cm, 60cm x 60cm...')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.area


class ProductColor(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='eg: White, Yellow, Red...')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images')

    origin = models.ForeignKey(ProductOrigin, on_delete=models.SET)
    type = models.ForeignKey(ProductType, on_delete=models.SET)
    area = models.ForeignKey(ProductArea, on_delete=models.SET)
    color = models.ForeignKey(ProductColor, on_delete=models.SET)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name[:50]

    def get_absolute_url(self):
        return reverse_lazy('products:detail', kwargs={'slug': self.slug})
