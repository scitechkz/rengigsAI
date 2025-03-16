from django.urls import path
from .views import sop_dashboard, api_sop_list

urlpatterns = [
    path("", sop_dashboard, name="sop_dashboard"),
    path("api/", api_sop_list, name="api_sop_list"),
   # path("upload/", upload_sop, name="upload_sop"),
]
