from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.enums import Countries
from apps.common.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(_('name'), max_length=100, unique=True, db_index=True)
    country = models.CharField(_('country'), max_length=10, choices=Countries.choices, default=Countries.ukr)

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')
        db_table = 'brands'

    def __str__(self):
        return self.name
