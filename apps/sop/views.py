from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SOPDocument

@login_required
def sop_dashboard(request):
    """Display SOP documents and AI chatbot interface."""
    sop_documents = SOPDocument.objects.all()
    return render(request, "sop/dashboard.html", {"sop_documents": sop_documents})

@user_passes_test(lambda u: u.is_staff)
def upload_sop(request):
    """Admin uploads SOP documents."""
    if request.method == "POST":
        title = request.POST["title"]
        document = request.FILES["document"]
        SOPDocument.objects.create(title=title, document=document, uploaded_by=request.user)
        return redirect("sop_dashboard")
    return render(request, "sop/upload.html")
