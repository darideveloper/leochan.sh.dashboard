from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profile, Experience, Education, SkillCategory, Skill, AeronauticalSkill, Interest, Language

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


class CVAPIExtensiveTestCase(APITestCase):
    def setUp(self):
        Profile.objects.all().delete()
        self.profile = Profile.get_solo()

    def test_empty_profile(self):
        """Test API response when the profile is empty."""
        response = self.client.get("/api/cv/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "")
        self.assertEqual(response.data["aboutMe"], "")
        self.assertEqual(response.data["contact"]["email"], "")
        self.assertEqual(response.data["technicalSkills"], [])
        self.assertEqual(response.data["education"], [])
        self.assertEqual(response.data["experience"], [])
        self.assertEqual(response.data["aeronautical"], [])
        self.assertEqual(response.data["interests"], [])
        self.assertEqual(response.data["languages"], [])

    def test_no_related_objects(self):
        """Test API response when profile exists but has no related objects."""
        self.profile.name = "Test User"
        self.profile.save()
        response = self.client.get("/api/cv/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test User")
        self.assertEqual(response.data["technicalSkills"], [])
        self.assertEqual(response.data["education"], [])

    def test_multiple_related_objects_and_ordering(self):
        """Test API returns multiple objects and respects order."""
        self.profile.name = "Test User"
        self.profile.save()
        Experience.objects.create(profile=self.profile, role="Second", order=2)
        Experience.objects.create(profile=self.profile, role="First", order=1)
        response = self.client.get("/api/cv/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["experience"]), 2)
        self.assertEqual(response.data["experience"][0]["role"], "First")
        self.assertEqual(response.data["experience"][1]["role"], "Second")

    def test_aeronautical_skill_interest_language_models(self):
        """Test serialization of AeronauticalSkill, Interest, and Language."""
        self.profile.name = "Test User"
        self.profile.save()
        AeronauticalSkill.objects.create(profile=self.profile, name="PPL", order=1)
        Interest.objects.create(profile=self.profile, name="Flying", order=1)
        Language.objects.create(profile=self.profile, name="English", level="Fluent", order=1)
        response = self.client.get("/api/cv/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["aeronautical"]), 1)
        self.assertEqual(response.data["aeronautical"][0], "PPL")
        self.assertEqual(len(response.data["interests"]), 1)
        self.assertEqual(response.data["interests"][0], "Flying")
        self.assertEqual(len(response.data["languages"]), 1)
        self.assertEqual(response.data["languages"][0]["name"], "English")

    def test_skill_without_details(self):
        """Test that a skill without details is handled correctly."""
        self.profile.name = "Test User"
        self.profile.save()
        cat = SkillCategory.objects.create(profile=self.profile, name="General", order=1)
        Skill.objects.create(category=cat, name="Communication", order=1)
        response = self.client.get("/api/cv/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["technicalSkills"][0]["skills"]), 1)
        self.assertEqual(response.data["technicalSkills"][0]["skills"][0]["details"], "")

    def test_education_with_single_line_details(self):
        """Test education details with a single line."""
        self.profile.name = "Test User"
        self.profile.save()
        Education.objects.create(profile=self.profile, details="Bachelor's Degree", order=1)
        response = self.client.get("/api/cv/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["education"]), 1)
        self.assertEqual(response.data["education"][0]["details"], ["Bachelor's Degree"])
