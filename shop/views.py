from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import sentry_sdk  # Импортируем SDK Sentry


def product_list(request, category_slug=None):
    '''Функция отображения каталога товаров'''
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)  # получаем товары которые есть в наличии
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug) # дополнительная фильтрация товаров по заданной категории
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug): # id и slug для извлечения экземпляра класса Product
    '''Функция отображения одного товара'''
    product = get_object_or_404(Product,
                                 id=id,
                                 slug=slug,
                                 available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


# Вызов Sentry Exception
class SentryTestExceptionView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Искусственно создаём исключение
            1 / 0
        except ZeroDivisionError as e:
            # Логируем исключение в Sentry
            sentry_sdk.capture_exception(e)
            return Response({"message": "Exception sent to Sentry."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
