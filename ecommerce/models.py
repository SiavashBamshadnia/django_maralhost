from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Car(Product):
    cylinder_count = models.PositiveSmallIntegerField()
    passenger_count = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=250)
    cylinder_volume = models.FloatField(validators=[MinValueValidator(0)])
    owner_name = models.CharField(max_length=250)

    class Meta:
        permissions = [
            ("search_car", "Can search between cars")
        ]
