from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from apps.api.models import Category
from apps.api.serializers.category_serializers import CategorySerializer
from helpers.mixins import PublicMixin
from helpers.repositories import GenericRepository

category_repository = GenericRepository(Category)


class CategoryViewSet(PublicMixin, viewsets.ModelViewSet):
    queryset = category_repository.get_all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name']
    pagination_class = None
