from django.contrib import admin
from django.urls import path, include
from .views import home  # Import home view

urlpatterns = [
    path("", home, name="home"),  # Root URL
    path("admin/", admin.site.urls),
    path("sop/", include("apps.sop.urls")),
    path("warehouse/", include("apps.warehouse.urls")),
    path("fleet/", include("apps.fleet.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
