from .cart import Cart


def cart(request):
    '''Функция для отображения корзины на главной странице'''
    return {'cart': Cart(request)}
