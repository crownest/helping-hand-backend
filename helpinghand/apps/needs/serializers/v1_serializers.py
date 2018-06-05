# Local Django
from .base_serializers import (
    NeedListSerializer, NeedCreateSerializer,
    NeedRetrieveSerializer, NeedUpdateSerializer, NeedItemListSerializer,
    NeedItemCreateSerializer,
)
from needs.models import Need, NeedItem


class NeedListSerializerV1(NeedListSerializer):
    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address',
                  'end_date', 'is_fixed', 'categories', 'supporters'
                  )


class NeedCreateSerializerV1(NeedCreateSerializer):
    pass


class NeedRetrieveSerializerV1(NeedRetrieveSerializer):
    pass


class NeedUpdateSerializerV1(NeedUpdateSerializer):
    pass


class NeedItemListSerializerV1(NeedItemListSerializer):
    pass


class NeedItemCreateSerializerV1(NeedItemCreateSerializer):
    pass
