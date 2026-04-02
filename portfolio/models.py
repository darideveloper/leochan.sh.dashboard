from django.db import models

class Technology(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="The name of the technology (e.g., Python, React).",
    )

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ("deployed", "Deployed"),
        ("in_development", "In Development"),
    ]

    id = models.SlugField(
        primary_key=True, help_text="Unique identifier for the project URL (slug)."
    )
    title = models.CharField(max_length=255, help_text="The name of the project.")
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        help_text="Cover image for the project.",
    )
    link = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the project's source code (e.g., GitHub, Gitea).",
    )
    preview = models.URLField(
        blank=True,
        null=True,
        help_text="URL to a live demo or production site.",
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="in_development",
        help_text="Current status of the project (e.g., Deployed, In Development).",
    )
    description = models.CharField(
        max_length=255, help_text="A short summary of the project for cards."
    )
    full_description = models.TextField(
        blank=True, help_text="A detailed overview for the sidebar."
    )
    content = models.TextField(help_text="Main body content of the project page (Markdown format).")
    date = models.CharField(
        max_length=255, help_text="Year or date range of the project (e.g., 2023)."
    )
    is_cv_highlight = models.BooleanField(
        default=False,
        help_text="If checked, this project will be highlighted in the CV section.",
    )
    technologies = models.ManyToManyField(
        Technology,
        related_name="projects",
        help_text="List of technologies used in this project.",
    )

    def __str__(self):
        return self.title

class ProjectTask(models.Model):
    project = models.ForeignKey(
        Project, related_name="tasks", on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=255,
        help_text="A specific task or achievement in this project (e.g., 'Coded in Arduino').",
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, help_text="Display order (lower numbers appear first)."
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Project Task"

    def __str__(self):
        return self.description
