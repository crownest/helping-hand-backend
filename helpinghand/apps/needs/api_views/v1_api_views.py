# Local Django
from .base_api_views import NeedViewSet
from needs.serializers import (
    NeedSerializer, NeedListSerializerV1,
    NeedCreateSerializerV1, NeedRetrieveSerializerV1
)


class NeedViewSetV1(NeedViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return NeedListSerializerV1
        elif self.action == 'create':
            return NeedCreateSerializerV1
        elif self.action == 'retrieve':
            return NeedRetrieveSerializerV1
        else:
            return NeedSerializer
