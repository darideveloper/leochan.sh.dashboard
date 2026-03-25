# admin-registration Specification

## Purpose
Define requirements for registering CV and Portfolio models in the Django admin interface with enhanced UI features and automatic sidebar navigation.

## ADDED Requirements
### Requirement: Register CV Models to Admin
All models in the `cv` application MUST be registered in the Django admin using `django-unfold` base classes.

#### Scenario: Register Profile as Singleton
- Model: `cv.models.Profile`
- Admin Class: Inherit from `unfold.contrib.solo.admin.SingletonModelAdmin`.
- Fields: All fields SHOULD be editable.

#### Scenario: Register SkillCategory and Skill
- Model: `cv.models.SkillCategory`
- Admin Class: Inherit from `unfold.admin.ModelAdmin`.
- Inlines: `Skill` SHOULD be managed as a `TabularInline` within `SkillCategory`.
- List Display: `name`, `order`.

#### Scenario: Register Experience, Education, and Language
- Models: `cv.models.Experience`, `cv.models.Education`, `cv.models.Language`.
- Admin Class: Inherit from `unfold.admin.ModelAdmin`.
- List Display: 
    - `Experience`: `role`, `company`, `date_range`, `order`.
    - `Education`: `institution`, `date_range`, `order`.
    - `Language`: `name`, `level`, `order`.
- Search Fields: `role`, `company`, `institution`, `name`.

### Requirement: Register Portfolio Models to Admin
All models in the `portfolio` application MUST be registered in the Django admin using `django-unfold` base classes.

#### Scenario: Register Technology
- Model: `portfolio.models.Technology`.
- Admin Class: Inherit from `unfold.admin.ModelAdmin`.
- List Display: `name`, `slug`.
- Search Fields: `name`.

#### Scenario: Register Project
- Model: `portfolio.models.Project`.
- Admin Class: Inherit from `unfold.admin.ModelAdmin`.
- List Display: `title`, `status`, `date`.
- List Filter: `status`, `technologies`.
- Search Fields: `title`, `description`.

### Requirement: Automatic Sidebar Navigation
The admin sidebar MUST automatically list registered applications and models without manual configuration.

#### Scenario: Remove Manual Sidebar Settings
Given `UNFOLD['SIDEBAR']['navigation']` is defined in `project/settings.py`
When the project is updated
Then `navigation` SHOULD be removed to allow Unfold to render all registered models automatically.
And `show_all_applications` SHOULD be set to `True`.
