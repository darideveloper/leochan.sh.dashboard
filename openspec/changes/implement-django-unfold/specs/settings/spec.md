# settings Specification Delta

## MODIFIED Requirements
### Requirement: Local and Third-Party App Configuration
The project MUST include all local apps and third-party dependencies in `INSTALLED_APPS`. `unfold` MUST be placed before `django.contrib.admin`.

#### Scenario: Register Unfold Apps
Given the `django-unfold` library is installed
When `settings.py` is initialized
Then `unfold`, `unfold.contrib.filters`, `unfold.contrib.forms`, and `unfold.contrib.inlines` SHOULD be included in `INSTALLED_APPS` **before** `django.contrib.admin`.

### Requirement: Admin Customization Settings
The project MUST define an `UNFOLD` dictionary for admin UI customization.

#### Scenario: Define UNFOLD Settings
Given `django-unfold` is used
When `settings.py` is initialized
Then it SHOULD contain an `UNFOLD` dictionary with `SITE_TITLE`, `SITE_HEADER`, `SITE_SUBHEADER`, `COLORS`, and `SIDEBAR` configurations.
