from django.db import models

# Create your models here.
class Labour(models.Model):
    name = models.CharField(max_length=2500)
    price = models.DecimalField(max_digits=6, decimal_places=2)