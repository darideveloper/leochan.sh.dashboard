# settings Spec Delta

## MODIFIED Requirements

### Requirement: Local and Third-Party App Configuration
The project MUST include all local apps and third-party dependencies in `INSTALLED_APPS`. `unfold` MUST be placed before `django.contrib.admin`.

#### Scenario: Register Storages App
- ADDED: `storages` MUST be included in `INSTALLED_APPS` for full functionality of `django-storages`.

### Requirement: Dynamic Database and Storage Selection
The project MUST support dynamic switching of database and storage based on environment variables.

#### Scenario: Configure AWS S3 for Production Storage
- MODIFIED: Storage settings MUST use the modern `STORAGES` dictionary format (introduced in Django 4.2).

## ADDED Requirements

### Requirement: Email Notifications Variable
The project SHALL standardize the environment variable name for the list of email recipients to `EMAILS_NOTIFICATIONS`.

#### Scenario: Standardize to EMAILS_NOTIFICATIONS
Standardize the environment variable name for the list of email recipients to `EMAILS_NOTIFICATIONS`.

### Requirement: Simplified Email SSL Configuration
The project MUST configure secure email connections using SSL as the preferred method.

#### Scenario: SSL-only Email Settings
`EMAIL_USE_SSL` SHOULD be the preferred method for secure email connection (typically Port 465), while `EMAIL_USE_TLS` SHOULD be removed to avoid confusion.

### Requirement: Docker Build-Time Configuration
The project MUST support build-time configuration for S3 storage and general environment settings.

#### Scenario: AWS ARGs in Dockerfile
The `Dockerfile` MUST include `ARG` and `ENV` for `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME`, `AWS_S3_REGION_NAME`, and `STORAGE_AWS` to support `collectstatic` during the build phase.
