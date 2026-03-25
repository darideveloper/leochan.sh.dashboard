# Design: Implement Django Unfold

## Architecture
Integrating `django-unfold` requires:
- Modifying `settings.py` to include `unfold` apps **before** `django.contrib.admin`.
- Defining a new `UNFOLD` configuration object in `settings.py` to control branding, colors, and navigation.
- Creating a `utils/callbacks.py` file to handle dynamic environment badges based on `ENV` environment variable.
- Adding custom scripts to `static/js/` to enhance UI elements (e.g., adding Tailwind classes, initializing SimpleMDE).
- Overriding the `admin/base.html` template in the project-wide `templates` directory.

## Trade-offs
- **Customization vs. Maintenance**: Extensive customization through `UNFOLD` settings and custom JS increases UI complexity but significantly improves UX.
- **Tailwind Dependency**: Custom JS (`add_tailwind_styles.js`) depends on Tailwind classes being available or correctly parsed by Unfold's internal Tailwind build.

## Patterns
- **Base Admin Class**: `ModelAdminUnfoldBase` will be used as a foundation for all future `ModelAdmin` classes to ensure consistent features like compressed fields and row actions.
- **Callbacks**: Using callbacks for environment-specific badges allows for dynamic UI changes without modifying the core Unfold settings on every environment switch.
