from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'shop'

    def ready(self):
        import shop.signals  # Импортируем файл сигналов