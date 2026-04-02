from rest_framework.test import APITestCase
from rest_framework import status
from .models import Project, Technology

class PortfolioAPITestCase(APITestCase):
    def setUp(self):
        Project.objects.all().delete()
        Technology.objects.all().delete()
        self.tech1 = Technology.objects.create(name="Python")
        self.tech2 = Technology.objects.create(name="React")
        
        self.project = Project.objects.create(
            id="test-project",
            title="Test Project",
            image="projects/test.png",
            status="deployed",
            description="Short desc",
            full_description="Full desc",
            content="# Markdown Content",
            date="2023"
        )
        self.project.technologies.add(self.tech1, self.tech2)

    def test_list_projects(self):
        """Test that /api/projects/ returns a list of project summaries."""
        # Note: This will only work after URLs are registered in Task 3
        response = self.client.get("/api/projects/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], "test-project")
        # Check absolute URL
        self.assertTrue(response.data[0]["image"].startswith("http"))
        # Human-readable status check
        self.assertEqual(response.data[0]["status"], "Deployed")

    def test_retrieve_project(self):
        """Test that /api/projects/{id}/ returns full project details."""
        # Note: This will only work after URLs are registered in Task 3
        response = self.client.get("/api/projects/test-project/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["fullDescription"], "Full desc")
        self.assertIn("Python", response.data["technologies"])
        self.assertIn("React", response.data["technologies"])
        self.assertEqual(response.data["content"], "# Markdown Content")
