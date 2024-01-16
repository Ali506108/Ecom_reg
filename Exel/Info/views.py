from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


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
