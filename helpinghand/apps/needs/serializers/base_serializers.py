# Third-Party
from rest_framework import serializers

# Local Django
from needs.models import Need
from users.serializers import UserListSerializer
from categories.serializers import CategoryListSerializer


class NeedSerializer(serializers.ModelSerializer):
    creator = UserListSerializer(read_only=True)
    supporters = UserListSerializer(many=True, read_only=True)
    categories = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address',
                  'end_date', 'is_fixed', 'creator', 'categories', 'supporters',
                  )


class NeedListSerializer(NeedSerializer):
    pass
