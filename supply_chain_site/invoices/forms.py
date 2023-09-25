from django import forms
from django.forms import ModelForm, inlineformset_factory #formset_factory

from .models import Invoice, ProductRow

class ProductRowForm(ModelForm):
    class Meta:
        model = ProductRow
        fields = ["product", "quantity", "row_description"]

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        #fields = ["customer",  "invoice_description", "product_rows",
        #          "invoice_created", "invoice_sent", "invoice_due_date"]
        fields = ["invoice_description", "invoice_created", "invoice_sent", "invoice_due_date"]

#InvoiceFormSet = formset_factory(CustomerForm, InvoiceForm, ProductRowForm, ProductForm)

ProductRowFormSet = inlineformset_factory(Invoice, ProductRow, 
                                       #fields=["product", "quantity", "row_description"])
                                       #form=[InvoiceForm, ProductRowForm])
                                       fields="__all__")


