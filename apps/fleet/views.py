from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Driver

@login_required(login_url='/accounts/login/')  # Ensure users log in first
def fleet_dashboard(request):
    """Show available drivers and fleet management system."""
    drivers = Driver.objects.filter(availability=True)
    return render(request, "fleet/dashboard.html", {"drivers": drivers})
