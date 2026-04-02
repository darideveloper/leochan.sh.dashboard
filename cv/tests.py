from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profile, Experience, Education, SkillCategory, Skill

class CVAPITestCase(APITestCase):
    def setUp(self):
        # Clear any existing profiles to ensure clean state
        Profile.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        SkillCategory.objects.all().delete()
        self.profile = Profile.get_solo()
        self.profile.name = "Léonard-Anton Llosa"
        self.profile.role = "Future Engineer"
        self.profile.email = "test@example.com"
        self.profile.phone = "+33 6 62 38 65 96"
        self.profile.linkedin = "https://linkedin.com/in/leo"
        self.profile.about_me = "Test About Me"
        self.profile.driving_license = "Category B"
        self.profile.save()

        # Skill Categories and Skills
        self.cat1 = SkillCategory.objects.create(profile=self.profile, name="SYSTEMS", order=1)
        Skill.objects.create(category=self.cat1, name="Automation", details="Ansible", order=1)

        # Experience
        Experience.objects.create(
            profile=self.profile,
            date_range="2025-2026",
            company="My Company",
            role="Engineer",
            order=1
        )

        # Education
        Education.objects.create(
            profile=self.profile,
            date_range="2024-2026",
            institution="University",
            details="Master's degree\nSpecialization in Networks",
            order=1
        )

    def test_get_cv_data(self):
        """Test that /api/cv/ returns the correct nested and flattened structure."""
        # Note: This will only work after URLs are registered in Task 3
        response = self.client.get("/api/cv/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertEqual(data["name"], "Léonard-Anton Llosa")
        self.assertEqual(data["aboutMe"], "Test About Me")
        
        # Test nested contact object
        self.assertEqual(data["contact"]["email"], "test@example.com")
        self.assertEqual(data["contact"]["drivingLicense"], "Category B")

        # Test technicalSkills structure
        self.assertEqual(len(data["technicalSkills"]), 1)
        self.assertEqual(data["technicalSkills"][0]["category"], "SYSTEMS")
        self.assertEqual(data["technicalSkills"][0]["skills"][0]["name"], "Automation")
        self.assertEqual(data["technicalSkills"][0]["skills"][0]["details"], "Ansible")

        # Test education details split
        self.assertEqual(len(data["education"]), 1)
        self.assertEqual(data["education"][0]["details"], ["Master's degree", "Specialization in Networks"])
