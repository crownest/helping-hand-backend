# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel


class Category(DateModel):
    name = models.CharField(verbose_name=_('Name'), max_length=254, unique=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return '{name}'.format(name=self.name)
