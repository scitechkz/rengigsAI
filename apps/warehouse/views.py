from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Rack
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RackSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated




@login_required(login_url='/accounts/login/')  # Ensure users log in first
def warehouse_dashboard(request):
    """Show warehouse racks and their status."""
    racks = Rack.objects.all()
    return render(request, "warehouse/dashboard.html", {"racks": racks})
#define API views using Django REST Framework.
@api_view(["GET"])
@permission_classes([IsAuthenticated])  # Requires valid JWT token
def api_rack_list(request):
    """Retrieve all warehouse racks (Authenticated Users Only)"""
    racks = Rack.objects.all()
    serializer = RackSerializer(racks, many=True)
    return Response(serializer.data)