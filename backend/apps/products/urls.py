from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from apps.products.views import ProductListRetrieveViewSet


app_name = 'products'

router = DefaultRouter()
router.register('products', ProductListRetrieveViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
