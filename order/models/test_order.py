import pytest
from django.contrib.auth.models import User

# Lembre-se de ajustar a importação abaixo de acordo com o nome do seu app
from order.models import Order
from product.models.product import Product


@pytest.fixture
def user():
    """Cria e retorna um usuário de teste."""
    return User.objects.create_user(username="testuser", password="testpassword123")


@pytest.fixture
def product_1():
    """Cria e retorna um produto de teste."""
    # Assumindo que seu Product tem campos como 'title' e 'price'. Ajuste conforme necessário.
    return Product.objects.create(title="Produto 1", price=50.00)


@pytest.fixture
def product_2():
    """Cria e retorna um segundo produto de teste."""
    return Product.objects.create(title="Produto 2", price=150.00)


# --- Testes ---


# A marcação @pytest.mark.django_db é OBRIGATÓRIA para testes
# que acessam o banco de dados no Django.
@pytest.mark.django_db
def test_create_order_with_products(user, product_1, product_2):
    """
    Testa a criação de um Order, garantindo que o User
    e os Products (ManyToMany) são atribuídos corretamente.
    """

    # 1. Cria a instância do pedido (Order) vinculada ao usuário
    order = Order.objects.create(user=user)

    # 2. Adiciona os produtos ao campo ManyToMany
    # (Não é possível adicionar no create() direto para ManyToMany)
    order.product.add(product_1, product_2)

    # 3. Asserções (Validações)
    assert Order.objects.count() == 1
    assert order.user == user
    assert order.user.username == "testuser"

    # Verifica se os produtos foram adicionados corretamente
    assert order.product.count() == 2
    assert product_1 in order.product.all()
    assert product_2 in order.product.all()


@pytest.mark.django_db
def test_order_cascade_delete_on_user(user, product_1):
    """
    Testa se o pedido é deletado quando o usuário é deletado
    (comportamento do on_delete=models.CASCADE).
    """
    order = Order.objects.create(user=user)
    order.product.add(product_1)

    assert Order.objects.count() == 1

    # Deleta o usuário
    user.delete()

    # Verifica se o pedido foi deletado em cascata
    assert Order.objects.count() == 0
