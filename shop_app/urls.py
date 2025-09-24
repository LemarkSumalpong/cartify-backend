from django.urls import path
from . import views

urlpatters = [
    path("products", views.products, name="products")
]