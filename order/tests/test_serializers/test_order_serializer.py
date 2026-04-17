from django.test import TestCase

from order.factories import OrderFactory
from product.factories import ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):

    def setUp(self):
        self.product_1 = ProductFactory(price=100)
        self.product_2 = ProductFactory(price=200)

        self.order = OrderFactory(
            product=[self.product_1, self.product_2]
        )

        self.serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        data = self.serializer.data

        # produtos
        self.assertEqual(data["product"][0]["title"], self.product_1.title)
        self.assertEqual(data["product"][1]["title"], self.product_2.title)

        # total
        self.assertEqual(data["total"], 300)