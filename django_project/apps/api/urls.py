from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.views.category_viewsets import CategoryViewSet
from apps.api.views.customer_viewsets import CustomerViewSet
from apps.api.views.order_viewsets import OrderViewSet
from apps.api.views.product_viewsets import ProductViewSet

app_name = "api"

router = DefaultRouter()

router.register("categories", CategoryViewSet, basename="categories")
router.register("products", ProductViewSet, basename="products")
router.register("customers", CustomerViewSet, basename="customers")
router.register("orders", OrderViewSet, basename="orders")


urlpatterns = [
    path('', include(router.urls)),
]
