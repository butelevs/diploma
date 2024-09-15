from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from .tasks import create_thumbnail  # Импорт задачи Celery


@receiver(post_save, sender=Product)
def create_product_thumbnail(sender, instance, **kwargs):
    """
    Эта функция вызывается после сохранения объекта Product и запускает задачу Celery
    для создания миниатюры изображения.
    """
    if instance.image:  # Проверка на наличие изображения
        create_thumbnail.delay(instance.image.path)  # Асинхронный вызов задачи
