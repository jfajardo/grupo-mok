from djoser.serializers import UserSerializer
from rest_framework import serializers

from apps.api.models import Order
from apps.api.serializers.customer_serializers import CustomerSerializer
from apps.api.serializers.product_serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    customer = CustomerSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        products = validated_data['products']
        del validated_data['products']
        order = Order.objects.create(
            user=user,
            **validated_data
        )
        order.products.set(products)
        return order