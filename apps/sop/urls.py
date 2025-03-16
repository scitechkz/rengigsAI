from django.urls import path
from .views import sop_dashboard

urlpatterns = [
    path("", sop_dashboard, name="sop_dashboard"),
   # path("upload/", upload_sop, name="upload_sop"),
]
