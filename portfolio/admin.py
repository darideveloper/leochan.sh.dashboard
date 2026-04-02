from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Technology, Project, ProjectTask
from project import admin as _

class ProjectTaskInline(TabularInline):
    model = ProjectTask
    extra = 1
    ordering_field = "order"
    hide_ordering_field = True
    list_display = ["description", "order"]

@admin.register(Technology)
class TechnologyAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ["title", "status", "date", "is_cv_highlight"]
    list_filter = ["status", "technologies", "is_cv_highlight"]
    search_fields = ["title", "description"]
    inlines = [ProjectTaskInline]
