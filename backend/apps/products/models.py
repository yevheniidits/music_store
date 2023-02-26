from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.enums import Countries
from apps.common.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(_('name'), max_length=100, unique=True, db_index=True)
    country = models.CharField(_('country'), max_length=10, choices=Countries.choices, default=Countries.ukr)
    parent_brand = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_brand')

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')
        db_table = 'brands'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(_('name'), max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(BaseModel):
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, related_name='products')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    title = models.CharField(_('title'), max_length=255)
    model_year = models.PositiveIntegerField(_('model year'))
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2)
    available = models.BooleanField(_('available'), default=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'products'
        ordering = ('category', 'brand', 'title')
        unique_together = ('brand', 'title', 'model_year')

    def __str__(self):
        return f'{self.brand.name} {self.title} {self.model_year}'
