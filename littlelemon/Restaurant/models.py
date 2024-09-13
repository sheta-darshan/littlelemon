from django.db import models
from django.core.validators import MaxValueValidator

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    booking_date = models.DateField()
    
    def __str__(self):
        return str(self.name)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MaxValueValidator(99999999.99)]  # Ensures maximum value is less than or equal to 99999999.99
    )
    inventory = models.IntegerField(validators=[MaxValueValidator(99999)])
    
    def __str__(self):
        return str(self.title)
