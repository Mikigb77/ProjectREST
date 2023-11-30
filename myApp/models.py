from django.db import models

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=600)

    def __str__(self) -> str:
        return self.name
