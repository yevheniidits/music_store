from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from apps.products.tests.factories import ProductFactory


class GetProductTestCase(APITestCase):
    client: APIClient
    maxDiff = None

    def test_list_product(self):
        ProductFactory.create_batch(4)
        url = reverse('products:products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 4)

    def test_retrieve_product(self):
        product = ProductFactory()
        url = reverse('products:products-detail', args=(product.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(
            response.json(),
            {
                'brand': product.brand.name,
                'category': product.category.name,
                'country': product.brand.country,
                'title': product.title,
                'model_year': product.model_year,
                'price': '1000.00',
                'available': product.available,
                'updated_at': datetime.strftime(product.updated_at, '%Y-%m-%dT%H:%M:%S.%fZ'),
            }
        )