from django.db import models
from solo.models import SingletonModel

class Profile(SingletonModel):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    linkedin = models.URLField()
    driving_license = models.CharField(max_length=255)
    about_me = models.TextField()

    def __str__(self):
        return "CV Profile"

    class Meta:
        verbose_name = "CV Profile"

class AeronauticalSkill(models.Model):
    profile = models.ForeignKey(Profile, related_name="aeronautical_skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Aeronautical Skill"

    def __str__(self):
        return self.name

class Interest(models.Model):
    profile = models.ForeignKey(Profile, related_name="interests", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

class SkillCategory(models.Model):
    profile = models.ForeignKey(Profile, related_name="skill_categories", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

class Experience(models.Model):
    profile = models.ForeignKey(Profile, related_name="experiences", on_delete=models.CASCADE)
    date_range = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name="educations", on_delete=models.CASCADE)
    date_range = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    details = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.institution} ({self.date_range})"

class Language(models.Model):
    profile = models.ForeignKey(Profile, related_name="languages", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} - {self.level}"
