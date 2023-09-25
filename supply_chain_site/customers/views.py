from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'customers/index.html'
    context_object_name = "latest_customers_list"

    def get_queryset(self):
        return Customer.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Customer
    template_name = "customers/detail.html"

class CreateView(generic.CreateView):
    model = Customer
    template_name = "customers/create.html"
    fields = ["name", "street_name", "city", "post_code", "phone_number", "email", 
    "contact_person", "contact_person_phone", "contact_person_phone"]
    success_url = "/customers"

class UpdateView(generic.UpdateView):
    model = Customer
    template_name = "customers/update.html"
    fields = ["name", "street_name", "city", "post_code", "phone_number", "email", 
    "contact_person", "contact_person_phone", "contact_person_phone"]

class DeleteView(generic.DeleteView):
    model = Customer
    template_name = "customers/delete.html"
    success_url = "/customers"
