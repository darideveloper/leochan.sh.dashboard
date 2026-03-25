from django.db import models
from solo.models import SingletonModel

class Profile(SingletonModel):
    name = models.CharField(
        max_length=255, help_text="Full name of the profile (e.g., LÉONARD-ANTON LLOSA)."
    )
    role = models.CharField(
        max_length=255,
        help_text="Professional title or current position (e.g., Future Network & Security Engineer).",
    )
    email = models.EmailField(help_text="Professional email address.")
    phone = models.CharField(
        max_length=50, help_text="Contact phone number (e.g., +33 6 62 38 65 96)."
    )
    linkedin = models.URLField(help_text="Link to your professional LinkedIn profile.")
    driving_license = models.CharField(
        max_length=255,
        help_text="Driving license status or category (e.g., Category B - Vehicle Owner).",
    )
    about_me = models.TextField(
        help_text="A short professional biography or 'About Me' section."
    )

    def __str__(self):
        return "CV Profile"

    class Meta:
        verbose_name = "CV Profile"

class AeronauticalSkill(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="aeronautical_skills", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        help_text="Aeronautical skill, certification, or experience (e.g., LAPL Student Pilot).",
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, help_text="Display order (lower numbers appear first)."
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Aeronautical Skill"

    def __str__(self):
        return self.name

class Interest(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="interests", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255, help_text="A personal interest or hobby (e.g., Aviation, Video Editing)."
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, help_text="Display order (lower numbers appear first)."
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

class SkillCategory(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="skill_categories", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255, help_text="The name of the skill category (e.g., SYSTEMS & DEVSECOPS)."
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, help_text="Display order (lower numbers appear first)."
    )

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory, related_name="skills", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255, help_text="The specific skill name (e.g., Automation)."
    )
    details = models.CharField(
        max_length=255,
        blank=True,
        help_text="Additional details or tools for this skill (e.g., Ansible, n8n).",
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, help_text="Display order (lower numbers appear first)."
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

class Experience(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="experiences", on_delete=models.CASCADE
    )
    date_range = models.CharField(
        max_length=255, help_text="The time period of the experience (e.g., 10/2025 – 08/2026)."
    )
    company = models.CharField(
        max_length=255, help_text="The name of the company or organization."
    )
    role = models.CharField(
        max_length=255, help_text="Your role or job title during this period."
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, help_text="Display order (lower numbers appear first)."
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="educations", on_delete=models.CASCADE
    )
    date_range = models.CharField(
        max_length=255, help_text="The time period of the education (e.g., 02/2024 – 06/2026)."
    )
    institution = models.CharField(
        max_length=255, help_text="The name of the school or university."
    )
    details = models.TextField(
        help_text="Specific details, degrees, or specializations (supports multiple lines)."
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, help_text="Display order (lower numbers appear first)."
    )

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.institution} ({self.date_range})"

class Language(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="languages", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255, help_text="The name of the language (e.g., English)."
    )
    level = models.CharField(
        max_length=255, help_text="Proficiency level (e.g., Native, TOEIC 940)."
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, help_text="Display order (lower numbers appear first)."
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} - {self.level}"
