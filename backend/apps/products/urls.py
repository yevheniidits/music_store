from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from apps.products.views import BrandListRetrieveViewSet


app_name = 'products'

router = DefaultRouter()
router.register('brands', BrandListRetrieveViewSet, basename='brands')

urlpatterns = [
    path('', include(router.urls)),
]
