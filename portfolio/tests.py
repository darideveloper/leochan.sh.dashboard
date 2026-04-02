from rest_framework.test import APITestCase
from rest_framework import status
from .models import Project, Technology, ProjectTask

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


class PortfolioAPIExtensiveTestCase(APITestCase):
    def setUp(self):
        Project.objects.all().delete()
        Technology.objects.all().delete()

    def test_no_projects(self):
        """Test API returns an empty list when there are no projects."""
        response = self.client.get("/api/projects/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_project_without_image(self):
        """Test project without an image returns null for the image field."""
        Project.objects.create(id="no-image-project", title="No Image Project")
        response = self.client.get("/api/projects/no-image-project/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNone(response.data["image"])

    def test_project_without_link_or_preview(self):
        """Test project without link or preview returns null for those fields."""
        Project.objects.create(id="no-link-project", title="No Link Project")
        response = self.client.get("/api/projects/no-link-project/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNone(response.data["link"])
        self.assertIsNone(response.data["preview"])

    def test_in_development_status(self):
        """Test 'in_development' status is correctly serialized."""
        Project.objects.create(id="dev-project", title="Dev Project", status="in_development")
        response = self.client.get("/api/projects/dev-project/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "In Development")

    def test_project_without_technologies(self):
        """Test project without technologies returns an empty list."""
        Project.objects.create(id="no-tech-project", title="No Tech Project")
        response = self.client.get("/api/projects/no-tech-project/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["technologies"], [])

    def test_project_task_serialization_and_ordering(self):
        """Test ProjectTask model serialization and ordering."""
        project = Project.objects.create(id="task-project", title="Task Project")
        ProjectTask.objects.create(project=project, description="Second Task", order=2)
        ProjectTask.objects.create(project=project, description="First Task", order=1)
        response = self.client.get("/api/projects/task-project/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["tasks"]), 2)
        self.assertEqual(response.data["tasks"][0], "First Task")
        self.assertEqual(response.data["tasks"][1], "Second Task")

    def test_is_cv_highlight_field(self):
        """Test is_cv_highlight field is correctly returned."""
        Project.objects.create(id="cv-project", title="CV Project", is_cv_highlight=True)
        Project.objects.create(id="not-cv-project", title="Not CV Project", is_cv_highlight=False)
        
        # Test retrieve for True
        response_true = self.client.get("/api/projects/cv-project/")
        self.assertEqual(response_true.status_code, status.HTTP_200_OK)
        self.assertTrue(response_true.data["isCvHighlight"])
        
        # Test retrieve for False
        response_false = self.client.get("/api/projects/not-cv-project/")
        self.assertEqual(response_false.status_code, status.HTTP_200_OK)
        self.assertFalse(response_false.data["isCvHighlight"])

    def test_404_not_found(self):
        """Test API returns 404 for a non-existent project."""
        response = self.client.get("/api/projects/non-existent-project/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
