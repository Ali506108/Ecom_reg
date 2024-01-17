from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm
from .models import Product


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, "Account created successfully. You can now log in."
            )
            return redirect("user_profile", username=user.username)
        else:
            messages.error(
                request, "Error in the form submission. Please check the form."
            )
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})


def user_profile(request, username):
    return render(request, "users/user_profile.html", {"username": username})


def filter_products(request):
    filtered_products = Product.objects.filter()
    filter_type = request.GET.get(
        "filter_type", "price"
    )  # Default to filtering by price

    if filter_type == "price":
        cheapest_products = Product.objects.order_by("price")[:5]
        most_expensive_products = Product.objects.order_by("-price")[:5]
    elif filter_type == "category":
        filtered_products = Product.objects.filter(category="Phone")
    elif filter_type == "categorys":
        filtered_products = Product.objects.filter(category="Air")
    else:
        filtered_products = Product.objects.all()

    context = {
        "filtered_products": filtered_products,
        "filter_type": filter_type,
    }

    context = {"filtered_products": filtered_products}

    return render(request, "users/your_template.html", context)
