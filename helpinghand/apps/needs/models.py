# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel


class Need(DateModel):
    # Base
    title = models.CharField(verbose_name=_('Title'), max_length=254)
    description = models.TextField(verbose_name=_('Description'))

    # Detail
    address = models.TextField(verbose_name=_('Address'))
    end_date = models.DateField(verbose_name=_('End Date'))
    is_fixed = models.BooleanField(verbose_name=_('Is Fixed'), default=False)

    # Relations
    creator = models.ForeignKey(
        verbose_name=_('Creator'), to='users.User',
        related_name='creator_needs', on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(
        verbose_name=_('Categories'), to='categories.Category',
        related_name='needs', blank=True
    )
    supporters = models.ManyToManyField(
        verbose_name=_('Supporters'), to='users.User',
        related_name='supporter_needs', blank=True
    )

    class Meta:
        verbose_name = _('Need')
        verbose_name_plural = _('Needs')

    def __str__(self):
        return '{title}'.format(title=self.title)


class NeedItem(DateModel):
    # Base
    name = models.CharField(verbose_name=_('Name'), max_length=254)

    # Detail
    remaining = models.CharField(
        verbose_name=_('Remaining'), max_length=254, blank=True
    )
    is_fixed = models.BooleanField(verbose_name=_('Is Fixed'), default=False)

    # Relations
    need = models.ForeignKey(
        verbose_name=_('Need'), to='needs.Need',
        related_name='need_items', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Need Item')
        verbose_name_plural = _('Need Items')
        unique_together = (('name', 'need'),)

    def __str__(self):
        return '{name}'.format(name=self.name)
