from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill 


class Category(models.Model):
    name = models.CharField(max_length=200)  # название категории
    slug = models.SlugField(max_length=200,   # создание индекса
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),  # индекс по полю name
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''Получение URL-адреса заданного объекта'''
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,  # внешний ключ к модели Category, взаимосвязь один ко многим, товар принадлежит к одной категории, категория содержит несколько товаров
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  # название товара
    slug = models.SlugField(max_length=200)  # для создания URL-адресов
    image = models.ImageField(upload_to='products/%Y/%m/%d', # изображение товара
                              blank=True)
    description = models.TextField(blank=True)  # описание товара
    price = models.DecimalField(max_digits=10,  # цена товара
                                decimal_places=2)
    available = models.BooleanField(default=True)  # наличие или отсутствие товара
    created = models.DateTimeField(auto_now_add=True)  # дата и время создания объекта
    updated = models.DateTimeField(auto_now=True)  # дата и время обновления объекта

    # Миниатюра, автоматически создаваемая ImageKit
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(100, 100)],
                               format='JPEG',
                               options={'quality': 60})

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),  # повышение производительности запросов
            models.Index(fields=['name']),  # индекс по полю name
            models.Index(fields=['-created']),  #  индекс по полю created определен в убывающем порядке
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''Получение URL-адреса заданного объекта'''
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
