# Third-Party
from rest_framework import routers

# Django
from django.conf.urls import url, include

# Local Django
from core.api_views import LoginViewV1
from needs.api_views import NeedViewSetV1, NeedItemViewSetV1
from users.api_views import UserViewSetV1

# Router V1
router_v1 = routers.DefaultRouter()
LIST_V1 = [
    (r'needs', NeedViewSetV1, 'needs'),
    (r'needitems', NeedItemViewSetV1, 'needitems'),
    (r'users', UserViewSetV1, 'users'),
]

for api in LIST_V1:
    router_v1.register(api[0], api[1], base_name=api[2])

urlpatterns = [
    url(r'v1/auth/login/', LoginViewV1.as_view(), name='auth-v1-login'),
    url(r'v1/auth/', include('djoser.urls.authtoken', namespace='auth-v1')),
    url(r'v1/', include((router_v1.urls, 'helpinghand'), namespace='v1'))
]
