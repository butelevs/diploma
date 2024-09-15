from django.urls import path
from . import views
from .views import SentryTestExceptionView

app_name = 'shop'

urlpatterns = [
    path('', views.product_list,
         name='product_list'),  # вызывает представление без параметров
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),  # параметр "category_slug", фильтровать товары с заданной категорией
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),  # параметр id и slug чтобы извлекать конкретный товар
    path('sentry-test-exception/', SentryTestExceptionView.as_view(), name='sentry_test_exception'),  # Sentry Exception
]
