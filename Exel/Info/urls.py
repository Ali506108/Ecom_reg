# Info/urls.py
from django.urls import path
from .views import filter_products, sign_up, user_profile

urlpatterns = [
    path("register/", sign_up, name="register"),
    path("user/<str:username>/", user_profile, name="user_profile"),
    path("filter/", filter_products, name="filter_products"),
    # Add other URL patterns as needed
]
