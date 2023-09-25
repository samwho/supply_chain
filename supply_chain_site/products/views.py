from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Product
from .forms import ProductForm

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = "latest_products_list"

    def get_queryset(self):
        return Product.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Product
    template_name = "products/detail.html"

class CreateView(generic.CreateView):
    model = Product
    template_name = "products/create_product.html"
    fields = ["product_name", "product_description", "price"]
    success_url = "/products"

class UpdateView(generic.UpdateView):
    model = Product
    template_name = "products/update_product.html"
    fields = ["product_name", "product_description", "price"]

class DeleteView(generic.DeleteView):
    model = Product
    template_name = "products/delete_product.html"
    success_url = "/products"


# Create your views here.
#def index(request):
#    latest_product_list = [p for p in Product.objects.all()][:5]
#    template = loader.get_template("products/index.html")
#    context = {
#            "latest_product_list": latest_product_list,
#            }
#    return render(request, "products/index.html", context)
#
#def detail(request, product_id):
#    product = get_object_or_404(Product, pk=product_id)
#    return render(request, "products/detail.html", {"product": product})
#def get_product(request):
#    if request.method == "POST":
#        form = ProductForm(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect("/products/")
#    else:
#        form = ProductForm()
#    return render(request, "products/product.html", {"form": form})

# following a guide
#def create_product(request):
#    context = {}
#    form = ProductForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#    context["form"] = form
#    return render(request, "products/create_product.html", context)

#def update_product(request, product_id):
#    context = {}
#    obj = get_object_or_404(Product, id = product_id)
#    form = ProductForm(request.POST or None, instance=obj)
#    if form.is_valid():
#        form.save()
#        return HttpResponseRedirect("/product/"+id)
#    context["form"] = form
#    return render(request, "products/update_product.html", context)
#
#
#def delete_product(request, product_id):
#    context = {}
#    obj = get_object_or_404(Product, id = product_id)
#    if request.method == "POST":
#        obj.delete()
#        return HttpResponseRedirect("/products/")
#    return render(request, "products/delete_product.html", context)
#
#
#