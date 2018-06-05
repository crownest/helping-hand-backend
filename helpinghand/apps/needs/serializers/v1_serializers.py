# Local Django
from .base_serializers import (
    NeedListSerializer, NeedCreateSerializer,
    NeedRetrieveSerializer, NeedUpdateSerializer
)
from needs.models import Need


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
