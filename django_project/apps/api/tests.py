from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from apps.api.models import Order, Product, Customer, Category


class OrderTestCase(TestCase):
    def setUp(self):
        # Crear objetos de prueba: una orden y algunos productos
        timestamp = int(datetime.now().timestamp())
        self.customer = Customer.objects.create(full_name=f'Customer test {timestamp}')
        self.user = User.objects.first()
        self.order = Order.objects.create(customer=self.customer, user=self.user)
        self.product1 = Product.objects.create(name=f'Product test {timestamp}', category_id=1)
        self.product2 = Product.objects.create(name=f'Other Product test {timestamp}', category_id=2)

    def test_add_products_to_order(self):
        # Obtener los productos de prueba
        products = [self.product1, self.product2]

        # Añadir los productos a la orden
        self.order.products.set(products)

        # Verificar que los productos fueron añadidos correctamente
        self.assertEqual(self.order.products.count(), 2)
        self.assertIn(self.product1, self.order.products.all())
        self.assertIn(self.product2, self.order.products.all())


class CategoryEndpointTestCase(TestCase):
    def setUp(self):
        # Crear objetos de prueba
        timestamp = int(datetime.now().timestamp())

        Category.objects.create(name=f'Category {timestamp}')
        Category.objects.create(name=f'Other Category {timestamp}')

        # Inicializar el cliente de prueba
        self.client = Client()

    def test_get_categories(self):
        # Hacer una solicitud GET al endpoint /categories
        response = self.client.get(reverse('api:categories-list'))

        # Verificar que la solicitud fue exitosa (código de estado 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar la respuesta JSON contiene las categorías esperadas
        expected_categories = Category.objects.all()
        self.assertEqual(response.json(), [{'id': category.id, 'name': category.name} for category in expected_categories])