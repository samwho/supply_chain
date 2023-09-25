from django.forms import ModelForm
from .models import Labour

class LabourForm(ModelForm):
    class Meta:
        model = Labour
        fields = ["name", "price"]
