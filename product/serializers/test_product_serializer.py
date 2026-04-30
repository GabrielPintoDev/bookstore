import pytest

from .product_serializer import ProductSerializer
from product.models import Product


@pytest.mark.django_db
def test_product_serializer():

    data = {
        "title": "Teste serializer",
        "description": "Testando o serializer",
        "price": 999,
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), f"Erros: {serializer.errors}"

    product = serializer.save()

    assert product.title == data["title"]  # Teste serializer
    assert product.description == data["description"]  # Testando o serializer
    assert product.price == data["price"]  # 999

    serializer = ProductSerializer(product)
    serialized_data = serializer.data

    assert serialized_data["title"] == data["title"]
    assert serialized_data["description"] == data["description"]
    assert serialized_data["price"] == data["price"]
