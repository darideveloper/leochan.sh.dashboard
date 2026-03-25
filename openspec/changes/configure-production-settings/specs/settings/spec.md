# Capability: Project Settings

Update `project/settings.py` to support multi-environment configuration, third-party apps, and custom local apps.

## MODIFIED Requirements

### Requirement: Local and Third-Party App Configuration
The project MUST include all local apps and third-party dependencies in `INSTALLED_APPS`.

#### Scenario: Register portfolio App
Given the `portfolio` app exists in the project
When `settings.py` is initialized
Then it SHOULD be included in `INSTALLED_APPS`.

#### Scenario: Register Third-Party Apps
Given `unfold`, `corsheaders`, `rest_framework`, and `solo` are installed
When `settings.py` is initialized
Then they SHOULD be included in `INSTALLED_APPS` and `MIDDLEWARE`.

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
