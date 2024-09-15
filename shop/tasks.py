from celery import shared_task
from PIL import Image
import os


@shared_task
def create_thumbnail(image_path):
    """
    Функция для создания миниатюры изображения.
    """
    size = (100, 100)  # Размер миниатюры
    image = Image.open(image_path)
    image.thumbnail(size)
    thumb_path = os.path.splitext(image_path)[0] + '_thumb.jpg'
    image.save(thumb_path, 'JPEG')

    return thumb_path
