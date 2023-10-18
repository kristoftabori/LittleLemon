from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField(null=True)

    def __str__(self) -> str:
        if self.no_of_guests > 0:
            return f"{self.name} and {str(self.no_of_guests)} on {self.booking_date}"
        return f"{self.name} alone on {self.booking_date}"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f"{self.title} : {str(self.price)}"

    def __str__(self) -> str:
        return self.title
