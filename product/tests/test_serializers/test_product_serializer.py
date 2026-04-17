from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.models import Product
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):

    def setUp(self):
        self.category = CategoryFactory(title="technology")

        self.product = ProductFactory(
            title="mouse",
            price=100,
            category=[self.category]
        )

        self.serializer = ProductSerializer(self.product)

    def test_product_serializer(self):
        data = self.serializer.data

        self.assertEqual(data["price"], 100)
        self.assertEqual(data["title"], "mouse")
        self.assertEqual(data["active"], self.product.active)

        self.assertEqual(
            data["category"][0]["title"],
            "technology"
        )

    def test_create_product(self):
        category = CategoryFactory()

        data = {
            "title": "keyboard",
            "description": "mechanical keyboard",
            "price": 300,
            "active": True,
            "categories_id": [category.id]
        }

        serializer = ProductSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        product = serializer.save()

        self.assertEqual(product.title, "keyboard")
        self.assertEqual(product.price, 300)

        # valida relação many-to-many
        self.assertEqual(product.category.count(), 1)
        self.assertEqual(product.category.first().id, category.id)