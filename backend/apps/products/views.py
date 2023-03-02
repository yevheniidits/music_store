from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.common.pagination import PageNumberPagination
from apps.products.serializers import ProductListSerializer
from apps.products.serializers import ProductRetrieveSerializer
from apps.products.models import Product


@extend_schema(
    tags=['Products'],
)
class ProductListRetrieveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.select_related('brand', 'category')
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer

        return ProductListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            return queryset.only('id', 'title', 'category__name', 'brand__name')

        return queryset.only(
            'brand__name',
            'category__name',
            'brand__country',
            'title',
            'model_year',
            'price',
            'available',
            'updated_at',
        )
