from django.db import models
from django.utils.translation import gettext_lazy as _


class Countries(models.TextChoices):
    usa = 'USA', _('USA')
    ukr = 'Ukraine', _('Ukraine')
    jap = 'Japan', _('Japan')
