from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        '''Функция для создания корзины'''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)  # получение корзины из текущего сеанса
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}  # сохранение пустой корзины в сеансе
        self.cart = cart

    def __iter__(self):
        '''Функция для получения товаров из базы данных'''
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        '''Функция для подсчета товара в корзине'''
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        '''Функция для добавления и/или обновления товаров в корзине'''
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        '''Функция для сохранения корзины в сеансе'''
        self.session.modified = True

    def remove(self, product):
        '''Функция для удаления товара из корзины'''
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        '''Функция для удаления корзины из сеанса'''
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        '''Функция для расчета общей стоимости товара в корзине'''
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())