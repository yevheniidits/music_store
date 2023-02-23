from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.products.serializers import BrandListSerializer
from apps.products.serializers import BrandRetrieveSerializer
from apps.products.models import Brand


@extend_schema(
    tags=['Products'],
)
class BrandListRetrieveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BrandRetrieveSerializer

        return BrandListSerializer

