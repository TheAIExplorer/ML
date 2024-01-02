from django.db import models

# Create your models here.
# car_classification/models.py


class CarBrand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
