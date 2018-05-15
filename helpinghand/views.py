# Django
from django.conf import settings
from django.views.static import serve
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.utils.translation import ugettext_lazy as _


class DocumentationView(View):

    def get(self, request, path='index.html', **kwargs):
        return serve(
            request, path, document_root=settings.DOCUMENTATION_ROOT, **kwargs
        )


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update({
            'title': _('Index'),
            'domain_documentation': '/docs/',
            'domain_admin_panel': '/admin/'
        })

        return context
