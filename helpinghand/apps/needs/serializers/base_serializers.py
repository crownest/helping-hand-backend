# Third-Party
from rest_framework import serializers

# Local Django
from needs.models import Need
from users.serializers import UserListSerializer
from categories.serializers import CategoryListSerializer


class NeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address',
                  'end_date', 'is_fixed', 'categories', 'supporters'
                  )


class NeedListSerializer(NeedSerializer):
    pass


class NeedCreateSerializer(NeedSerializer):
    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address',
                  'end_date', 'is_fixed', 'categories', 'supporters'
                  )

