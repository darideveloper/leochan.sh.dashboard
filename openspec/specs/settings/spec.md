# settings Specification

## Purpose
TBD - created by archiving change configure-production-settings. Update Purpose after archive.
## Requirements
### Requirement: Local and Third-Party App Configuration
The project MUST include all local apps and third-party dependencies in `INSTALLED_APPS`. `unfold` MUST be placed before `django.contrib.admin`.

#### Scenario: Register Unfold Apps
Given the `django-unfold` library is installed
When `settings.py` is initialized
Then `unfold`, `unfold.contrib.filters`, `unfold.contrib.forms`, and `unfold.contrib.inlines` SHOULD be included in `INSTALLED_APPS` **before** `django.contrib.admin`.

### Requirement: Dynamic Database and Storage Selection
The project MUST support dynamic switching of database and storage based on environment variables.

#### Scenario: Use SQLite for Development
Given `ENV` is set to `dev` in `.env`
When the database configuration is loaded
Then it SHOULD default to a SQLite database.

#### Scenario: Configure AWS S3 for Production Storage
Given `STORAGE_AWS` is set to `True` in the environment
When storage settings are initialized
Then they SHOULD use the AWS S3 backend provided by `django-storages`.

### Requirement: Admin Customization Settings
The project MUST define an `UNFOLD` dictionary for admin UI customization.

#### Scenario: Define UNFOLD Settings
Given `django-unfold` is used
When `settings.py` is initialized
Then it SHOULD contain an `UNFOLD` dictionary with `SITE_TITLE`, `SITE_HEADER`, `SITE_SUBHEADER`, `COLORS`, and `SIDEBAR` configurations.

