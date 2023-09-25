from django.shortcuts import render
from .models import Vendor
#from .forms import VendorForm 
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'vendors/index.html'
    context_object_name = "latest_vendors_list"

    def get_queryset(self):
        return Vendor.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Vendor 
    template_name = "vendors/detail.html"

class CreateView(generic.CreateView):
    model = Vendor
    template_name = "vendors/create.html"
    fields = ["name", "email", "phone", "contact_person",
              "contact_person_phone", "contact_person_email", "speciality"] 
    success_url = "/vendors"

class UpdateView(generic.UpdateView):
    model = Vendor
    template_name = "vendors/update.html"
    fields = ["name", "email", "phone", "contact_person",
              "contact_person_phone", "contact_person_email", "speciality"] 

class DeleteView(generic.DeleteView):
    model = Vendor
    template_name = "vendors/delete.html"
    success_url = "/vendors"
