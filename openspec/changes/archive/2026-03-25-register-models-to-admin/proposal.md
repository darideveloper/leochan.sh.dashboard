# Proposal: Register CV and Portfolio Models to Admin

## Goal
Register all models from `cv/` and `portfolio/` applications in the Django admin interface using `django-unfold` for an enhanced management experience. This includes setting up appropriate filters, search fields, and display options for each model, and removing manual sidebar configurations to allow for automatic model listing.

## Why
Currently, models in `cv/` and `portfolio/` are not registered in the admin, which prevents data management via the dashboard. Additionally, the manual `UNFOLD['SIDEBAR']['navigation']` configuration in `project/settings.py` is causing `NoReverseMatch` errors because it references admin URLs for unregistered models. Removing the manual configuration will resolve these errors and provide a cleaner, more maintainable sidebar that automatically updates as models are added or modified.

## Capabilities
- **CV Admin Registration**: Register `Profile`, `SkillCategory`, `Skill`, `Experience`, `Education`, and `Language` models with Unfold-compatible `ModelAdmin` classes.
- **Portfolio Admin Registration**: Register `Technology` and `Project` models with advanced filtering and search capabilities.
- **Automatic Sidebar Navigation**: Update `UNFOLD` settings to remove manual navigation and enable automatic application listing.

## Relationship
- **Depends On**: `define-cv-and-portfolio-models` (already implemented) and `implement-django-unfold` (already implemented).
- **Impacts**: Admin dashboard UI and model management workflows.
