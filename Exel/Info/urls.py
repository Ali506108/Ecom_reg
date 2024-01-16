# Info/urls.py
from django.urls import path
from .views import sign_up, user_profile

urlpatterns = [
    path("register/", sign_up, name="register"),
    path("user/<str:username>/", user_profile, name="user_profile"),
    # Add other URL patterns as needed
]
