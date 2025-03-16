from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Driver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DriverSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated




@login_required(login_url='/accounts/login/')  # Ensure users log in first
def fleet_dashboard(request):
    """Show available drivers and fleet management system."""
    drivers = Driver.objects.filter(availability=True)
    return render(request, "fleet/dashboard.html", {"drivers": drivers})
#define API for fleet
@api_view(["GET"])
@permission_classes([IsAuthenticated])  # Requires valid JWT token
def api_driver_list(request):
    """Retrieve all available drivers (Authenticated Users Only)"""
    drivers = Driver.objects.filter(availability=True)
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)