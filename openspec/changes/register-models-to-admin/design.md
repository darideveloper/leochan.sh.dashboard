# Design: Register CV and Portfolio Models to Admin

## Overview
Registering all models from the `cv/` and `portfolio/` applications in the Django admin interface, utilizing `django-unfold` features to provide a modern, feature-rich management dashboard.

## Technical Strategy
- **Base Admin Class**: Use `unfold.admin.ModelAdmin` as the base for all registered models to ensure consistency with the Unfold theme.
- **Singleton Management**: For the `Profile` model (which uses `solo.models.SingletonModel`), use `unfold.contrib.solo.admin.SingletonModelAdmin` to manage the single record efficiently.
- **Inlines**: Implement `unfold.admin.TabularInline` or `StackedInline` where appropriate (e.g., `Skill` within `SkillCategory`) to simplify data entry for related models.
- **Filters and Search**: Enhance the `Project` and `Experience` models with filters (e.g., `status`, `company`) and search fields to improve discoverability in the admin.
- **Dynamic Sidebar**: Simplify the `UNFOLD` configuration in `project/settings.py` by removing the manual `navigation` list and setting `show_all_applications` to `True` (if applicable) or letting Unfold default to its automatic application listing.

## Patterns and Components
- **List Display**: Configure `list_display` for all models to show relevant fields (e.g., `title`, `status`, `company`, `order`).
- **Ordering**: Set `ordering` to reflect the `order` field in models where applicable.
- **Search Fields**: Add `search_fields` for primary textual data (e.g., `title`, `name`, `company`).

## Trade-offs and Considerations
- **Automatic Sidebar vs Manual**: While a manual sidebar allows for fine-grained control, an automatic one is more robust and easier to maintain in the early stages of development.
- **Inline Depth**: Limit inlines to direct relationships to maintain admin performance and UI clarity.
