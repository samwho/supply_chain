from django.urls import path

from . import views

urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("<int:pk>/", views.DetailView.as_view(), name="detail"),
        #path("get_product/", views.get_product, name="get_product"),

        # following a guide
        path("create/", views.CreateView.as_view(), name="create_labour"),
        path("update/<int:pk>", views.UpdateView.as_view(), name="update_labour"),
        path("delete/<int:pk>", views.DeleteView.as_view(), name="delete_labour")
        ]
