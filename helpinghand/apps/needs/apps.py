# Django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NeedsConfig(AppConfig):
    name = 'needs'
    verbose_name = _('Needs')
