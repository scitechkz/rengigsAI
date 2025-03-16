from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    """Handles user registration"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the new user
            return redirect("home")  # Redirect to homepage
    else:
        form = UserCreationForm()  # Ensure form is created properly

    return render(request, "users/signup.html", {"form": form})  # Pass form to template
