from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "street_name", "city", "post_code", "phone_number", "email", 
                  "contact_person", "contact_person_phone", "contact_person_email"]
