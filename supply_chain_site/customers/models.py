from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=2500)
    street_name = models.CharField(max_length=1500)
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=2500)
    contact_person = models.CharField(max_length=1500)
    contact_person_phone = models.CharField(max_length=20)
    contact_person_email = models.CharField(max_length=2500)

