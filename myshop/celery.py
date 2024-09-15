from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Стандартный модуль настроек Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')  # Переменная для командной строки
app = Celery('myshop')  # Экземпляр приложения
app.config_from_object('django.conf:settings', namespace='CELERY')  # Загрузка конфигураций
app.autodiscover_tasks()  # Обнаружение асинхронных заданий в приложениях