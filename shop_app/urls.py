from django.urls import path
from . import views

urlpatterns = [
    path("products", views.products, name="products"),
]

# fecthing all_products: https://127.0.0.1:800/product/