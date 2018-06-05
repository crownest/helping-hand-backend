# Local Django
from .base_api_views import NeedViewSet, NeedItemViewSet
from needs.serializers import (
    NeedSerializer, NeedListSerializerV1,
    NeedCreateSerializerV1, NeedRetrieveSerializerV1,
    NeedUpdateSerializerV1, NeedItemSerializer,
    NeedItemListSerializer, NeedItemCreateSerializer,
)


class NeedViewSetV1(NeedViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return NeedListSerializerV1
        elif self.action == 'create':
            return NeedCreateSerializerV1
        elif self.action == 'retrieve':
            return NeedRetrieveSerializerV1
        elif self.action == 'update':
            return NeedUpdateSerializerV1
        else:
            return NeedSerializer


class NeedItemViewSetV1(NeedItemViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return NeedItemListSerializer
        elif self.action == 'create':
            return NeedItemCreateSerializer
        else:
            return NeedItemSerializer
