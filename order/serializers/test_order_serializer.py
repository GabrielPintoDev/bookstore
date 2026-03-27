import pytest
from django.contrib.auth.models import User
# Ajuste as importações para os caminhos reais do seu projeto
from order.models import Order 
from product.models.product import Product
from order.serializers import OrderSerializer

# --- Fixtures ---

@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="testpassword123")

@pytest.fixture
def product_1():
    return Product.objects.create(title="Teclado", price=150.00)

@pytest.fixture
def product_2():
    return Product.objects.create(title="Mouse", price=50.00)

@pytest.fixture
def order(user, product_1, product_2):
    """Cria um pedido com dois produtos para testar a serialização."""
    order = Order.objects.create(user=user)
    order.product.add(product_1, product_2)
    return order

# --- Testes ---

@pytest.mark.django_db
def test_order_serializer_fields_and_total(order, product_1, product_2, user):
    """
    Testa se o serializer retorna os campos corretos e 
    se o cálculo do 'total' está preciso.
    """
    # 1. Instancia o serializer
    serializer = OrderSerializer(instance=order)
    
    # 2. Gera o dicionário de saída
    data = serializer.data
    
    # 3. Asserções
    
    # Verifica se todos os campos esperados estão no dicionário
    assert "product" in data
    assert "user" in data
    assert "total" in data  # Isso falharia com o seu código original!
    
    # Verifica se os valores básicos estão corretos
    assert data["user"] == user.id
    assert len(data["product"]) == 2
    
    # Valida a lógica principal do get_total (150.00 + 50.00)
    expected_total = product_1.price + product_2.price
    assert data["total"] == expected_total

@pytest.mark.django_db
def test_order_serializer_empty_products(user):
    """
    Testa o comportamento do serializer e do cálculo do 'total' 
    quando um pedido não tem produtos associados.
    """
    order = Order.objects.create(user=user)
    serializer = OrderSerializer(instance=order)
    
    data = serializer.data
    
    # Como não há produtos, o total deve ser 0
    assert len(data["product"]) == 0
    assert data["total"] == 0