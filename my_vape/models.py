from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Vape(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.brand} - {self.age}"