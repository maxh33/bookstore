import json

from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from product.factories import CategoryFactory
from product.models import Category

class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='GPU')

    def test_get_all_category(self):
        url = f"/bookstore/v1/category/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

        self.assertEqual(category_data["results"][0]['title'], self.category.title)

    def test_create_category(self):
        data = json.dumps({
            'title': 'CPU',
        })

        url = f"/bookstore/v1/category/"
        response = self.client.post(
            url,
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_category = Category.objects.get(title='CPU')

        self.assertEqual(created_category.title, 'CPU')