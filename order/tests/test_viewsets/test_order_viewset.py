import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import ProductFactory, CategoryFactory
from product.models import Product

class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self. category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        self.order = OrderFactory(product=[self.product])
        token = Token.objects.create(user=self.order.user)
        token.save()

    def test_order(self):
        token = Token.objects.get(user__username=self.order.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        
        # Use the full URL pattern including the 'bookstore/' prefix
        url = f"/bookstore/v1/order/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)

        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"], self.product.active
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
        token = Token.objects.get(user__username=self.order.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({"product_id": [product.id], "user": user.id})

        # Use the full URL pattern including the 'bookstore/' prefix
        url = f"/bookstore/v1/order/"
        response = self.client.post(
            url,
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)