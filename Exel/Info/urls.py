# Info/urls.py
from django.urls import path
from .views import filter_products, sign_up, user_profile, add_product

urlpatterns = [
    path("register/", sign_up, name="register"),
    path("user/<str:username>/", user_profile, name="user_profile"),
    path("filter/", filter_products, name="filter_products"),
    path("add_product/", add_product, name="add_product"),
]
