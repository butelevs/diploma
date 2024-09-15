"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Тюнинг админки
    path("admin/", admin.site.urls),  # Базовая админка
    path('cart/', include('cart.urls', namespace='cart')),  # Приложение для покупательской корзины
    path('orders/', include('orders.urls', namespace='orders ')),  # Приложение для оформления заказа
    path('', include('shop.urls', namespace='shop')),  # Основное приложение магазина
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Схема OpenAPI
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # ReDoc UI
    path('auth/', include('social_django.urls', namespace='social')),  # авторизация с соц.сетью VK
    path('sentry-test-exception/', include('shop.urls', namespace='sentry-test-exception')),  # Sentry
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)