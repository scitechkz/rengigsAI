from django.contrib import admin
from django.urls import path, include
from .views import home  # Import home view
from django.contrib.auth import views as auth_views
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("sop/", include("apps.sop.urls")),
    path("warehouse/", include("apps.warehouse.urls")),
    path("fleet/", include("apps.fleet.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),  # Explicit redirect
    path("users/", include("apps.users.urls")),  # Add this line
    
    
      # JWT Authentication Endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
