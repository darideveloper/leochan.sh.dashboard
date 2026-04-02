from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Project
from .serializers import ProjectSummarySerializer, ProjectDetailSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for the Project model.
    Exposes project list and details at /api/projects/.
    """
    permission_classes = [AllowAny]
    pagination_class = None
    queryset = Project.objects.all().prefetch_related("technologies")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProjectDetailSerializer
        return ProjectSummarySerializer
