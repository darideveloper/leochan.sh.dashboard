from rest_framework import serializers
from .models import (
    Profile, AeronauticalSkill, Interest, SkillCategory, Skill,
    Experience, Education, Language
)
from portfolio.models import Project

class CVProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="description"
    )

    class Meta:
        model = Project
        fields = ["title", "tasks"]

class CVDataSerializer(serializers.ModelSerializer):
    contact = serializers.SerializerMethodField()
    aboutMe = serializers.CharField(source="about_me")
    aeronautical = serializers.SerializerMethodField()
    interests = serializers.SerializerMethodField()
    technicalSkills = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "name",
            "role",
            "contact",
            "aboutMe",
            "aeronautical",
            "interests",
            "technicalSkills",
            "experience",
            "education",
            "languages",
            "projects",
        ]

    def get_contact(self, obj):
        return {
            "email": obj.email,
            "phone": obj.phone,
            "linkedin": obj.linkedin,
            "drivingLicense": obj.driving_license,
        }

    def get_aeronautical(self, obj):
        return list(obj.aeronautical_skills.values_list("name", flat=True))

    def get_interests(self, obj):
        return list(obj.interests.values_list("name", flat=True))

    def get_technicalSkills(self, obj):
        categories = obj.skill_categories.all().prefetch_related("skills")
        return [
            {
                "category": cat.name,
                "skills": [
                    {"name": s.name, "details": s.details} for s in cat.skills.all()
                ],
            }
            for cat in categories
        ]

    def get_experience(self, obj):
        return [
            {"date": exp.date_range, "company": exp.company, "role": exp.role}
            for exp in obj.experiences.all()
        ]

    def get_education(self, obj):
        return [
            {
                "date": edu.date_range,
                "institution": edu.institution,
                "details": [
                    line.strip() for line in edu.details.split("\n") if line.strip()
                ],
            }
            for edu in obj.educations.all()
        ]

    def get_languages(self, obj):
        return [
            {"name": lang.name, "level": lang.level} for lang in obj.languages.all()
        ]

    def get_projects(self, obj):
        projects = Project.objects.filter(is_cv_highlight=True).prefetch_related("tasks")
        return CVProjectSerializer(projects, many=True).data
