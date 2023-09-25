from django.urls import path

from . import views

urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("get_invoice/", views.get_invoice, name="get_invoice"),
        path("create_invoice/", views.create_invoice, name="create_invoice")
        ]
