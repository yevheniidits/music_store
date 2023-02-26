from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.products.serializers import ProductListSerializer
from apps.products.serializers import ProductRetrieveSerializer

from apps.products.models import Product


@extend_schema(
    tags=['Products'],
)
class ProductListRetrieveViewSet(viewsets.ReadOnlyModelViewSet):
    # TODO optimize queries
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer

        return ProductListSerializer
