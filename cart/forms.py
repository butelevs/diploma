from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
#
#
# class CartAddProductForm(forms.Form):
#     '''Добавление товаров в корзину'''
#     quantity = forms.TypedChoiceField(  # позволяет пользователю выбирать кол-во от 1 до 20
#                                 choices=PRODUCT_QUANTITY_CHOICES,
#                                 coerce=int)
#     override = forms.BooleanField(required=False,  # позволяет прибавлять или переопределять товар в корзине
#                                   initial=False,
#                                   widget=forms.HiddenInput)


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)