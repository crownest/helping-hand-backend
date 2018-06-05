# Local Django
from .base_serializers import NeedListSerializer, NeedCreateSerializer
from users.serializers import UserListSerializerV1
from categories.serializers import CategoryListSerializerV1
from needs.models import Need


class NeedListSerializerV1(NeedListSerializer):

    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address',
                  'end_date', 'is_fixed', 'categories', 'supporters'
                  )


class NeedCreateSerializerV1(NeedCreateSerializer):
    pass
