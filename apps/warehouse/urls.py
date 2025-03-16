from django.urls import path
from .views import warehouse_dashboard, api_rack_list

urlpatterns = [
    path("", warehouse_dashboard, name="warehouse_dashboard"),
    path("api/", api_rack_list, name="api_rack_list"),
]
