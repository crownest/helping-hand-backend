# Local Django
from .base_api_views import NeedViewSet
from needs.serializers import (
    NeedSerializer, NeedListSerializer, NeedListSerializerV1
)


class NeedViewSetV1(NeedViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return NeedListSerializerV1
