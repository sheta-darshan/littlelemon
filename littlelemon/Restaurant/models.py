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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def __str__(self):
        return str(self.title)
