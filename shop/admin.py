from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # отображаемые поля
    prepopulated_fields = {'slug': ('name',)}  # указывает поле, значение которого устанавливается автоматически с использованием значения другого поля


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',  # отображаемые поля
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']  # фильтрация по полям
    list_editable = ['price', 'available']  # редактируемые поля
    prepopulated_fields = {'slug': ('name',)}  # указывает поле, значение которого устанавливается автоматически с использованием значения другого поля