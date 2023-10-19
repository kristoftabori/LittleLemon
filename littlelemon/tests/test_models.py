from django.test import TestCase
from restaurant.models import Booking, Menu
from datetime import date

class BookingTest(TestCase):
    input_dict = {
        "name": "Joe Tester",
        "no_of_guests": 15,
        "booking_date": date(
            year=2010,
            month=10,
            day=19,
        ),
    }
    def test_instance_created(self):
        my_instance = Booking.objects.create(
            name=self.input_dict["name"],
            no_of_guests=self.input_dict["no_of_guests"],
            booking_date=self.input_dict["booking_date"],
        )
        self.assertTrue(
            my_instance.name == "Joe Tester" and
            my_instance.no_of_guests == 15 and
            my_instance.booking_date == date(
                year=2010,
                month=10,
                day=19,
            )
        )

class MenuItemTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")