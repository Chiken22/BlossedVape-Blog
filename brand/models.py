from unicodedata import name
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=40)
    url = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.url}"