from django.contrib import admin
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin, TabularInline
from .models import Profile, SkillCategory, Skill, Experience, Education, Language

@admin.register(Profile)
class ProfileAdmin(SingletonModelAdmin, ModelAdmin):
    pass

class SkillInline(TabularInline):
    model = Skill
    extra = 1

@admin.register(SkillCategory)
class SkillCategoryAdmin(ModelAdmin):
    list_display = ["name", "order"]
    inlines = [SkillInline]

@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    list_display = ["role", "company", "date_range", "order"]
    search_fields = ["role", "company"]
    list_filter = ["company"]

@admin.register(Education)
class EducationAdmin(ModelAdmin):
    list_display = ["institution", "date_range", "order"]
    search_fields = ["institution"]

@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    list_display = ["name", "level", "order"]
    search_fields = ["name"]
