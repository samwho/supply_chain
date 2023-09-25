from django.db import models

from products.models import Product
from customers.models import Customer


# Create your models here.

class Invoice(models.Model):
    customer = models.ForeignKey(
            Customer,
            on_delete=models.CASCADE
            )
    product_rows = models.ManyToManyField(Product, through="ProductRow")
    invoice_description = models.CharField(max_length=2500)
    invoice_created = models.DateField()
    invoice_sent = models.DateField()
    invoice_due_date = models.DateField()

    def __str__(self):
        return self.invoice_description

class ProductRow(models.Model):
    product = models.ForeignKey(
            Product,
            on_delete=models.CASCADE
            )
    invoice = models.ForeignKey(
            Invoice,
            on_delete=models.CASCADE
            )
    quantity = models.DecimalField(max_digits=20, decimal_places=10)
    row_description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.row_description

#class CreateInvoiceAllFields(models.Model):



