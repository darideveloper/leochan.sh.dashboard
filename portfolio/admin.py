from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Technology, Project

@admin.register(Technology)
class TechnologyAdmin(ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ["title", "status", "date", "is_cv_highlight"]
    list_filter = ["status", "technologies", "is_cv_highlight"]
    search_fields = ["title", "description"]
