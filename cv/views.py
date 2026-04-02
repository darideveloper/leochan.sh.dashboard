from rest_framework import viewsets, response
from rest_framework.permissions import AllowAny
from .models import Profile
from .serializers import CVDataSerializer

class CVViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for the singleton Profile model.
    Exposes CV data at /api/cv/.
    """
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = CVDataSerializer

    def list(self, request, *args, **kwargs):
        instance = Profile.get_solo()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = Profile.get_solo()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)
