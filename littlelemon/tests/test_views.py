from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from restaurant.serializers import MenuItemSerializer

class MenuViewTEst(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=50, inventory=20)
        Menu.objects.create(title="Burger", price=30, inventory=50)
    
    def test_get_all_menu_items(self):
        response = self.client.get(reverse('menu-list'))
        menu_items = Menu.objects.all
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        