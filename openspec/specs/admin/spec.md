# admin Specification

## Purpose
TBD - created by archiving change implement-django-unfold. Update Purpose after archive.
## Requirements
### Requirement: Unfold-Compatible Admin Base Class
The project MUST provide a base `ModelAdmin` class compatible with `django-unfold` features.

#### Scenario: Use Unfold ModelAdmin Base
Given a custom model exists in the project
When a `ModelAdmin` is registered for that model
Then it SHOULD inherit from `ModelAdminUnfoldBase` (which inherits from `unfold.admin.ModelAdmin`) to enable row actions, compressed fields, and other Unfold UI features.

### Requirement: Custom Auth Admin
The `User` model MUST be registered with a `django-unfold` compatible admin class.

#### Scenario: Register User with Unfold Admin
Given `django.contrib.auth.models.User` is in use
When `admin.site` is initialized
Then `User` SHOULD be registered with a subclass of `unfold.admin.ModelAdmin`.

### Requirement: Custom Admin Templates and Assets
The project MUST override the default admin templates to include custom scripts and styles.

#### Scenario: Inject Custom Assets in Admin
Given `project/templates/admin/base.html` exists
When the admin dashboard is loaded
Then it SHOULD include `add_tailwind_styles.js`, `load_markdown.js`, and `range_date_filter_es.js` to enhance the Unfold interface.

