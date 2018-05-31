# Local Django
from .base_serializers import NeedListSerializer
from users.serializers import UserListSerializerV1
from categories.serializers import CategoryListSerializerV1
from needs.models import Need


class NeedListSerializerV1(NeedListSerializer):
    creator = UserListSerializerV1(read_only=True)
    supporters = UserListSerializerV1(many=True, read_only=True)
    categories = CategoryListSerializerV1(many=True, read_only=True)

    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address', 'end_date',
                  'is_fixed', 'creator', 'categories', 'supporters'
                  )
