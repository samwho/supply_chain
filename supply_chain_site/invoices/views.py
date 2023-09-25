from django.shortcuts import render
from django.template import loader
from django.views import generic
from .models import Invoice
from .forms import InvoiceForm, ProductRowForm#, InvoiceFormSet
from products.forms import ProductForm 
from customers.forms import CustomerForm 

from django.forms import ModelForm, formset_factory

# Create your views here.

# inline formset factory
# https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d

# JS for adding and removing
# https://stackoverflow.com/questions/61135510/add-row-dynamically-in-django-formset

# m2m forms
# https://openclassrooms.com/en/courses/7107341-intermediate-django/7265468-create-many-to-many-relationships

#def index(request):
#    latest_invoice_list = [i for i in Invoice.objects.all()][:5]
#    template = loader.get_template("invoices/index.html")
#    context = {
#            "latest_invoice_list": latest_invoice_list,
#            }
#    return render(request, "invoices/index.html", context)
#
def get_invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/invoices/")
    else:
        form = InvoiceForm()

    return render(request, "invoices/invoice.html", {"form": form})

class IndexView(generic.ListView):
    model = Invoice
    template_name = "invoices/index.html"

def create_invoice(request):
    '''
    customer = Customer.objects.create('some_parameter')
    customer.save()
    invoice = Invoice.objects.create('some_parameter')
    invoice.customer.add(customer)
    created_product_rows = []
    for product_row in product_rows:

        
    

    '''
    customer_form = CustomerForm(request.POST)
    invoice_form = InvoiceForm(request.POST)
    product_form = ProductForm(request.POST)
    product_row_form = ProductRowForm(request.POST)
    return render(request, "invoices/invoice.html", { "invoice_form": invoice_form, 
                                                      "customer_form": customer_form, 
                                                      "product_form": product_form,
                                                      "product_row_form": product_row_form })
#def create_invoice(request):
#    customer_form = CustomerForm(request.POST)
#    invoice_form = InvoiceForm(request.POST)
#    # Probably need an inline set to create many of these
#    product_form = ProductForm(request.POST)
#    # Probably need an inline set to create many of these
#    product_row_form = ProductRowForm(request.POST)
#    if request.method == "POST":
#        if all([customer_form.is_valid(), product_form.is_valid(), invoice_form.is_valid(), 
#                product_row_form.is_valid()]):
#            customer = customer_form.save(commit=False)
#            invoice = invoice_form.save(commit=False)
#            product = product_form.save(commit=False)
#            product_row = product_row_form.save(commit=False)
#            product_row.product.add(product)
#            invoice.customer.add(customer)
#            invoice.product_row.add(product_row)
#            invoice.save()
#    return render(request, "invoices/invoice.html", { "invoice_form": invoice_form, 
#                                                      "customer_form": customer_form, 
#                                                      "product_form": product_form,
#                                                      "product_row_form": product_row_form })
    #invoice = Invoice.objects.get(request)
    # THIS IS SUPPOSED TO BE THE CHILD!
    # https://swapps.com/blog/working-with-nested-forms-with-django/
    #invoice_form_set = InvoiceFormSet(invoice, request.POST)
    #return render(request, "invoice/invoice.html", {"invoiceForm": invoice_form_set})
    #invoice_form_set = InvoiceFormSet(request.POST) 
    #if request.method == "POST":
    #    invoice_form_set = InvoiceFormSet(request.POST, request.FILES)
    #    if invoice_form_set.is_valid():
    #        return HttpResponseRedirect("/invoices/")
    #else:
    #    invoice_form_set = InvoiceFormSet()

    #return render(request, "invoices/invoice.html", {"invoiceForm": invoice_form_set}) 

#def create_invoice(request):
#    invoiceForm = formset_factory(InvoiceForm)
#    #customerForm = CustomerForm(request.POST)
#    #productForm = ProductForm(request.POST)
#    #productRowForm = ProductRowForm(request.POST)
#    if request.method == "POST":
#        #formset = InvoiceFormSet(request.POST, request.FILES)
#        customerForm = CustomerForm(request.POST, request.FILES)
#        invoiceForm = InvoiceForm(request.POST, request.FILES)
#        productForm = ProductForm(request.POST, request.FILES)
#        productRowForm = ProductRowForm(request.POST, request.FILES)
#        if invoiceForm.is_valid() & productForm.is_valid() \
#            & customerForm.is_valid() & productRowForm.is_valid():
#            # do something with the formset.cleaned_data
#            return HttpResponseRedirect("/invoices/")
#    else:
#        #formset = InvoiceFormSet()
#        invoiceForm = InvoiceForm()
#        customerForm = CustomerForm()
#        productForm = ProductForm()
#        productRowForm = ProductRowForm()
#    return render(request, "invoices/invoice.html", { "invoiceForm": invoiceForm, 
#                                                      "customerForm": customerForm, 
#                                                      "productForm": productForm,
#                                                      "productRowForm": productRowForm })
#