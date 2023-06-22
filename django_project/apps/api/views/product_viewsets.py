from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from apps.api.models import Product
from apps.api.serializers.product_serializers import ProductSerializer
from helpers.mixins import AuthMixin


class ProductViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', ]
