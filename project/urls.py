from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework import routers
from cv.views import CVViewSet
from portfolio.views import ProjectViewSet

# Initialize DRF Router
router = routers.DefaultRouter()
router.register(r"cv", CVViewSet, basename="cv")
router.register(r"projects", ProjectViewSet, basename="projects")

urlpatterns = [
    # Admin Interface
    path("admin/", admin.site.urls),
    # Root Redirect to Admin
    path(
        "",
        RedirectView.as_view(url="/admin/portfolio/project/"),
        name="home-redirect-admin",
    ),
    # API Endpoints
    path("api/", include(router.urls)),
    path("api/", include("shared.urls")),
]

# Serve Media Files in Development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
