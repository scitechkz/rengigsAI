from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SOPDocument

@login_required(login_url='/accounts/login/')  # Ensure users log in first
def sop_dashboard(request):
    """Display SOP documents and AI chatbot interface."""
    sop_documents = SOPDocument.objects.all()
    return render(request, "sop/dashboard.html", {"sop_documents": sop_documents})
