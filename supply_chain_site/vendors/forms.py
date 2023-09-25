from django.forms import ModelForm
from .models import Vendor 

class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ["name", "email", "phone", "contact_person",
                  "contact_person_phone", "contact_person_email", "speciality"]