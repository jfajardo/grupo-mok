from rest_framework import viewsets, status

from apps.api.models import Order
from apps.api.serializers.order_serializers import OrderSerializer, OrderCreateSerializer, OrderDetailSerializer
from helpers.mixins import AuthMixin
from helpers.repositories import GenericRepository
from rest_framework.response import Response

order_repository = GenericRepository(Order)


class OrderViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = order_repository.get_all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        elif self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def create(self, request, *args, **kwargs):
        try:
            serializer = OrderCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                data = serializer.save()
                serializer = OrderDetailSerializer(data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
