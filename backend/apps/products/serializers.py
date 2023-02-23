from rest_framework import serializers

from apps.products.models import Brand


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'country',
        )


class BrandRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'country',
            'created_at',
            'updated_at',
        )
