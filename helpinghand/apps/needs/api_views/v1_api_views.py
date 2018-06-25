# Local Django
from .base_api_views import NeedViewSet, NeedItemViewSet
from needs.serializers import (
    NeedSerializer, NeedListSerializerV1,
    NeedCreateSerializerV1, NeedRetrieveSerializerV1,
    NeedUpdateSerializerV1, NeedItemSerializer,
    NeedItemListSerializerV1, NeedItemCreateSerializerV1,
    NeedItemUpdateSerializerV1, NeedItemRetrieveSerializerV1,
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
            return NeedItemListSerializerV1
        elif self.action == 'create':
            return NeedItemCreateSerializerV1
        elif self.action == 'retrieve':
            return NeedItemRetrieveSerializerV1
        elif self.action == 'update':
            return NeedItemUpdateSerializerV1
        else:
            return NeedItemSerializer
