from django.contrib import admin
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from .models import (
    Profile, 
    SkillCategory, 
    Skill, 
    Experience, 
    Education, 
    Language,
    AeronauticalSkill,
    Interest
)

class AeronauticalSkillInline(TabularInline):
    model = AeronauticalSkill
    extra = 1
    ordering_field = "order"
    hide_ordering_field = True
    list_display = ["name", "order"]

class InterestInline(TabularInline):
    model = Interest
    extra = 1
    ordering_field = "order"
    hide_ordering_field = True
    list_display = ["name", "order"]

class LanguageInline(TabularInline):
    model = Language
    extra = 1
    ordering_field = "order"
    hide_ordering_field = True
    list_display = ["name", "order"]

class ExperienceInline(TabularInline):
    model = Experience
    extra = 1
    ordering_field = "order"
    hide_ordering_field = True
    list_display = ["role", "company", "order"]

class EducationInline(StackedInline):
    model = Education
    extra = 1
    ordering_field = "order"
    hide_ordering_field = True
    list_display = ["institution", "order"]

@admin.register(Profile)
class ProfileAdmin(SingletonModelAdmin, ModelAdmin):
    inlines = [
        AeronauticalSkillInline, 
        InterestInline, 
        LanguageInline,
        ExperienceInline,
        EducationInline
    ]

class SkillInline(TabularInline):
    model = Skill
    extra = 1
    ordering_field = "order"
    hide_ordering_field = True
    list_display = ["name", "order"]

@admin.register(SkillCategory)
class SkillCategoryAdmin(ModelAdmin):
    list_display = ["name", "order"]
    list_editable = ["order"]
    inlines = [SkillInline]
