# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel
from users.models import User


class Need(DateModel):
    title = models.CharField(verbose_name=_('Title'), max_length=254)
    description = models.TextField(verbose_name=_('Description'))
    address = models.TextField(verbose_name=_('Address'))
    end_date = models.DateField(verbose_name=_('End Date'))
    is_fixed = models.BooleanField(verbose_name=_('Is Fixed'), default=False)
    creator = models.ForeignKey(
        verbose_name=_('Creator'), to=User, related_name='creator_needs', on_delete=models.CASCADE
    )
    supporters = models.ManyToManyField(verbose_name=_('Supporters'), to=User, related_name='supporter_needs')

    class Meta:
        verbose_name = _('Need')
        verbose_name_plural = _('Needs')

    def __str__(self):
        return '{title}'.format(title=self.title)


class NeedItem(DateModel):
    name = models.CharField(verbose_name=_('Name'), max_length=254)
    is_fixed = models.BooleanField(verbose_name=_('Is Fixed'), default=False)
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
