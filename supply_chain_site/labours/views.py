from django.shortcuts import render
from .models import Labour
from .forms import LabourForm 
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'labours/index.html'
    context_object_name = "latest_labours_list"

    def get_queryset(self):
        return Labour.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Labour 
    template_name = "labours/detail.html"

class CreateView(generic.CreateView):
    model = Labour
    template_name = "labours/create.html"
    fields = ["name", "price"] 
    success_url = "/labours"

class UpdateView(generic.UpdateView):
    model = Labour
    template_name = "labours/update.html"
    fields = ["name", "price"] 

class DeleteView(generic.DeleteView):
    model = Labour
    template_name = "labours/delete.html"
    success_url = "/labours"
