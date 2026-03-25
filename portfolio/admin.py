from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Technology, Project
from project import admin as _

@admin.register(Technology)
class TechnologyAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ["title", "status", "date", "is_cv_highlight"]
    list_filter = ["status", "technologies", "is_cv_highlight"]
    search_fields = ["title", "description"]
