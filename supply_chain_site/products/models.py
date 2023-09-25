from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length = 500)
    product_description = models.CharField(max_length = 2500)
    price = models.DecimalField(max_digits=20, decimal_places=4)

    def __str__(self):
        return self.product_name

