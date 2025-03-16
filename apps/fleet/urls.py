from django.urls import path
from .views import fleet_dashboard, api_driver_list

urlpatterns = [
    path("", fleet_dashboard, name="fleet_dashboard"),
    path("api/", api_driver_list, name="api_driver_list"),
]
