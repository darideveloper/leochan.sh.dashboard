from rest_framework import serializers
from .models import Project, Technology

class ProjectSummarySerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display")
    isCvHighlight = serializers.BooleanField(source="is_cv_highlight")

    class Meta:
        model = Project
        fields = ["id", "title", "image", "link", "preview", "status", "isCvHighlight"]

class ProjectDetailSerializer(ProjectSummarySerializer):
    fullDescription = serializers.CharField(source="full_description")
    technologies = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    tasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='description'
     )

    class Meta:
        model = Project
        fields = ProjectSummarySerializer.Meta.fields + [
            "description",
            "fullDescription",
            "content",
            "technologies",
            "date",
            "tasks",
        ]
