from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Rack

@login_required(login_url='/accounts/login/')  # Ensure users log in first
def warehouse_dashboard(request):
    """Show warehouse racks and their status."""
    racks = Rack.objects.all()
    return render(request, "warehouse/dashboard.html", {"racks": racks})
