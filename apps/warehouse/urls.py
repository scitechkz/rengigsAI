from django.urls import path
from .views import warehouse_dashboard

urlpatterns = [
    path("", warehouse_dashboard, name="warehouse_dashboard"),
]
