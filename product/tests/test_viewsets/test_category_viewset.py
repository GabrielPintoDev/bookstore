from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self):
        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # ✅ suporta paginação ou não
        if isinstance(data, dict):
            data = data["results"]

        self.assertEqual(data[0]["title"], self.product.title)
        self.assertEqual(data[0]["price"], self.product.price)
        self.assertEqual(data[0]["active"], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()

        data = {"title": "notebook", "price": 800.00, "categories_id": [category.id]}

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}), data=data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="notebook")

        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800.00)
