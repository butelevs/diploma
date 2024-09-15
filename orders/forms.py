from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    '''Класс для создания новых объектов заказа'''
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
