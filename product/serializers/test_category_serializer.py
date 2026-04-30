import pytest

# Lembre-se de ajustar os caminhos de importação conforme o seu projeto
from product.models.category import Category

# Substitua o caminho abaixo pelo local exato do seu serializer
from product.serializers.category_serializer import CategorySerializer

# --- Fixtures ---


@pytest.fixture
def category():
    """Cria e retorna uma categoria de teste padrão."""
    return Category.objects.create(
        title="Livros",
        slug="livros",
        description="Livros de diversos gêneros",
        active=True,
    )


# --- Testes ---


@pytest.mark.django_db
def test_category_serializer_serialization(category):
    """
    Testa a transformação de uma instância de Category em um dicionário (Leitura).
    """
    # Instancia o serializer com o objeto do banco de dados
    serializer = CategorySerializer(instance=category)
    data = serializer.data

    # Verifica se os campos declarados no Meta.fields estão presentes
    expected_keys = {"title", "slug", "description", "active"}
    assert set(data.keys()) == expected_keys

    # Valida se os dados exportados correspondem ao objeto
    assert data["title"] == category.title
    assert data["slug"] == category.slug
    assert data["description"] == category.description
    assert data["active"] == category.active


@pytest.mark.django_db
def test_category_serializer_deserialization():
    """
    Testa o recebimento de dados, validação e criação de uma nova Category (Escrita).
    """
    # Simula um payload JSON (dicionário) vindo de uma requisição POST
    valid_data = {
        "title": "Jogos de Tabuleiro",
        "slug": "jogos-de-tabuleiro",
        "description": "Jogos para a família",
        "active": True,
    }

    # Instancia o serializer passando os dados para validação
    serializer = CategorySerializer(data=valid_data)

    # 1. Verifica se os dados são válidos segundo as regras do modelo
    assert serializer.is_valid() is True

    # 2. Salva o objeto no banco de dados
    new_category = serializer.save()

    # 3. Confirma se o objeto foi persistido corretamente
    assert new_category.id is not None
    assert Category.objects.count() == 1
    assert new_category.title == valid_data["title"]


@pytest.mark.django_db
def test_category_serializer_invalid_deserialization():
    """
    Testa se o serializer bloqueia dados inválidos, como a falta de um campo obrigatório.
    """
    # O campo 'title' é obrigatório no modelo (não possui null=True/blank=True).
    # Vamos enviar um payload sem ele para forçar um erro.
    invalid_data = {"slug": "sem-titulo", "active": True}

    serializer = CategorySerializer(data=invalid_data)

    # Verifica se o serializer aponta que os dados são inválidos
    assert serializer.is_valid() is False

    # Verifica se o erro está atrelado ao campo correto ('title')
    assert "title" in serializer.errors
