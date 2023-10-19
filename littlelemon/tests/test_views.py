from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.views import MenuItemView


class MenuItemsViewTest(TestCase):

    MENU_ITEMS = [
        {
            "title": "Bruschetta",
            "price": "7.20",
            "inventory": 15
        },
        {
            "title": "Tomato Soup",
            "price": "10.30",
            "inventory": 25
        },
        {
            "title": "Tiramisu",
            "price": "9.80",
            "inventory": 100
        }
    ]

    USERS = [
        {
            "username": "Maniac Testing",
            "password": "employee123",
        },
    ]

    MENU_ITEMS_URL = "http://localhost:8000/api/menu-items/"

    def setUp(self) -> None:

        for user in self.USERS:
            User.objects.create_user(username=user["username"], password=user["password"])
        
        for item in self.MENU_ITEMS:
            Menu.objects.create(
                title=item["title"],
                price=item["price"],
                inventory=item["inventory"],
            )

    def test_authenticated_get(self):
        self.assertTrue(len(User.objects.all()) == 1)
        self.assertTrue(len(Menu.objects.all()) == 3)
        self.assertTrue(
            self.client.login(
                username=self.USERS[0]["username"],
                password=self.USERS[0]["password"],
            )
        )
        response = self.client.get(self.MENU_ITEMS_URL)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data),len(self.MENU_ITEMS))
        original = [item["title"] for item in self.MENU_ITEMS]
        retrieved = [item["title"] for item in response.data]
        self.assertTrue(all([orig == ret for orig, ret in zip(original, retrieved)]))

        
        