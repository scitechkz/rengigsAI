from django.shortcuts import render
def home(request):
    """Homepage for Rengigs"""
    return render(request, "home.html")