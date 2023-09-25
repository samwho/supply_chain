from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=2500)
    email = models.CharField(max_length=2500)
    phone = models.CharField(max_length=10)
    contact_person = models.CharField(max_length=2500)
    contact_person_phone = models.CharField(max_length=10)
    contact_person_email = models.CharField(max_length=2500)
    speciality = models.JSONField()