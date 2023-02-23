from django.db import models
from django.utils.translation import gettext_lazy as _


class Countries(models.TextChoices):
    usa = 'Usa', _('United States of America')
    ukr = 'Ukr', _('Ukraine')
