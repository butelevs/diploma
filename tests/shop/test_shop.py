import pytest
from shop.models import Category, Product
from django.urls import reverse
from shop.factories import CategoryFactory, ProductFactory


@pytest.fixture
def category_factory(db):
    def create_category(**kwargs):
        return Category.objects.create(**kwargs)
    return create_category


@pytest.fixture
def product_factory(db, category_factory):
    def create_product(**kwargs):
        # Указываем значения по умолчанию для обязательных полей
        if 'price' not in kwargs:
            kwargs['price'] = 10.0  # Указываем цену по умолчанию
        if 'name' not in kwargs:
            kwargs['name'] = 'Default Product Name'
        if 'category' not in kwargs:
            kwargs['category'] = category_factory(name='Default Category', slug='default-category')  # Создаем категорию по умолчанию
        return Product.objects.create(**kwargs)
    return create_product


@pytest.mark.django_db
def test_product_list_view(client):
    category = CategoryFactory(name='Test Category', slug='test-category')
    product1 = ProductFactory(name='Product 1', category=category, available=True, price=25.0)
    product2 = ProductFactory(name='Product 2', available=True, price=30.0)

    response = client.get(reverse('shop:product_list'))
    assert response.status_code == 200
    assert product1 in response.context['products']
    assert product2 in response.context['products']


@pytest.mark.django_db
def test_product_detail_view(client):
    product = ProductFactory(name='Test Product', slug='test-product', available=True, price=50.0)

    response = client.get(reverse('shop:product_detail', args=[product.id, product.slug]))
    assert response.status_code == 200
    assert response.context['product'] == product
    assert 'cart_product_form' in response.context
