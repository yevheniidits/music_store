from rest_framework import serializers

from apps.products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'brand',
            'category',
            'title',
        )


class ProductRetrieveSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    country = serializers.CharField(source='brand.country', read_only=True)

    class Meta:
        model = Product
        fields = (
            'brand',
            'category',
            'country',
            'title',
            'model_year',
            'price',
            'available',
            'updated_at',
        )
