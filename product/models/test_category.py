import pytest

# Lembre-se de ajustar a importação para o caminho correto do seu projeto
from product.models import Category

# --- Fixtures ---


@pytest.fixture
def category():
    """Cria e retorna uma categoria de teste padrão."""
    return Category.objects.create(
        title="Eletrônicos",
        slug="eletronicos",
        description="Produtos tecnológicos e gadgets",
        # Não passamos o 'active' para testar o valor default
    )


# --- Testes ---


@pytest.mark.django_db
def test_category_creation(category):
    """
    Testa se a categoria é criada corretamente e se os campos
    salvam os dados esperados.
    """
    assert Category.objects.count() == 1
    assert category.title == "Eletrônicos"
    assert category.slug == "eletronicos"
    assert category.description == "Produtos tecnológicos e gadgets"


@pytest.mark.django_db
def test_category_default_active_field(category):
    """
    Testa se o campo 'active' recebe True por padrão,
    conforme definido no modelo.
    """
    assert category.active is True


@pytest.mark.django_db
def test_category_unicode_representation(category):
    """
    Testa se o método __unicode__ retorna o título da categoria.
    (Nota: Se você alterar para __str__, mude a chamada aqui também).
    """
    assert category.__unicode__() == "Eletrônicos"

    # Se você atualizar seu modelo para def __str__(self):
    # o teste correto seria:
    # assert str(category) == "Eletrônicos"
