from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ("deployed", "Deployed"),
        ("in_development", "In Development"),
    ]

    id = models.SlugField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    preview = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="in_development")
    description = models.CharField(max_length=255)
    full_description = models.TextField(blank=True)
    content = models.TextField(help_text="Markdown content")
    date = models.CharField(max_length=255)
    is_cv_highlight = models.BooleanField(default=False)
    technologies = models.ManyToManyField(Technology, related_name="projects")

    def __str__(self):
        return self.title
