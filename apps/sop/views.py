from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SOPDocument
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SOPDocumentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated




@login_required(login_url='/accounts/login/')  # Ensure users log in first
def sop_dashboard(request):
    """Display SOP documents and AI chatbot interface."""
    sop_documents = SOPDocument.objects.all()
    return render(request, "sop/dashboard.html", {"sop_documents": sop_documents})

#define API views using Django REST Framework.
@api_view(["GET"])
@permission_classes([IsAuthenticated])  # Requires valid JWT token
def api_sop_list(request):
    """Retrieve all SOP documents (Authenticated Users Only)"""
    sop_documents = SOPDocument.objects.all()
    serializer = SOPDocumentSerializer(sop_documents, many=True)
    return Response(serializer.data)