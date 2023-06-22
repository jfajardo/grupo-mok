from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from apps.api.models import Customer
from apps.api.serializers.customer_serializers import CustomerSerializer
from helpers.mixins import AuthMixin


class CustomerViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['full_name', 'identification', 'phone']
