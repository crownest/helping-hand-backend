"""helpinghand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# Django
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url, include

#  Local Django
from helpinghand.views import DocumentationView, IndexView, ActivationView, ResetPasswordView
from core.api_views import LoginView

urlpatterns = [
    # Landing
    url(r'^$', IndexView.as_view(), name='index'),

    #  Admin
    url(r'^admin/', admin.site.urls),

    # Documentation
    url(r'^docs/$', DocumentationView.as_view(), name='docs'),
    url(r'^docs/(?P<path>.*)$', DocumentationView.as_view(), name='docs'),

    #  Api
    url(r'^api/', include('helpinghand.api_urls')),

    # Token
    url(r'^auth/login', LoginView.as_view(), name='login'),
    url(r'^auth/', include('djoser.urls.authtoken')),

    # Activation and Password Operations
    url(r'^activation/(?P<key>\w+)/$', ActivationView.as_view(), name='activation'),
    url(r'^reset-password/(?P<key>\w+)/$', ResetPasswordView.as_view(), name='reset-password')
]

# Media
if settings.DEBUG:
    urlpatterns += (
        url(r'media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
