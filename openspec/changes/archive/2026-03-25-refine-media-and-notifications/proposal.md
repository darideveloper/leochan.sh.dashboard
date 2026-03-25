---
change-id: refine-media-and-notifications
description: Synchronize environment variables, storage configuration, Dockerfile, and documentation.
---

# Proposal: Refine Media and Notifications Configuration

This change synchronizes the project's environment variables, Docker configuration, and Django settings with the documentation and best practices. It fixes inconsistencies in email notification variables, enables required Django apps for storage, enhances the Docker build process for S3 support, and updates all related documentation.

## Requirements

### [Requirement: Unify Email Notification Variables]
Standardize the environment variable for email notifications across settings, environment files, and documentation.

#### [Scenario: Standardize to `EMAILS_NOTIFICATIONS`]
- Replace `EMAILS_LEADS_NOTIFICATIONS` in `settings.py` with `EMAILS_NOTIFICATIONS`.
- Replace `EMAILs_NOTIFICATIONS` (incorrect casing/plurality) in `.env.prod`, `.env.dev`, and `docs/project-setup.md` with `EMAILS_NOTIFICATIONS`.
- Update all documentation references to use `EMAILS_NOTIFICATIONS`.

### [Requirement: Complete Django Storages Integration]
Ensure the `django-storages` backend is fully integrated into the Django application lifecycle.

#### [Scenario: Enable `storages` in `INSTALLED_APPS`]
- Add `"storages"` to `INSTALLED_APPS` in `project/settings.py`.
- Ensure the app is correctly initialized by Django to handle custom storage backends.

### [Requirement: Update Media Storage Documentation]
Correct the documentation to accurately reflect the project structure and modern Django storage settings.

#### [Scenario: Fix Project Name and Settings in Storage Guide]
- Replace all instances of `nyx_dashboard` with `project` in `docs/media-file-storage.md`.
- Ensure the code examples in the documentation match the `STORAGES` dictionary implementation used in `project/settings.py`.

### [Requirement: Cleanup Email and Environment Settings]
Remove obsolete settings and ensure production consistency.

#### [Scenario: Remove `EMAIL_USE_TLS`]
- Remove `EMAIL_USE_TLS` logic from `project/settings.py` as requested (SSL is preferred).
- Remove `EMAIL_USE_TLS` from `.env.prod`, `.env.dev`, and `docs/project-setup.md`.

#### [Scenario: Add Missing S3 Variables]
- Add `AWS_S3_ENDPOINT_URL` to the expected environment variables in the project's S3 configuration logic and environment files to support S3-compatible providers like DigitalOcean Spaces.

### [Requirement: Production Readiness for Docker]
Ensure the `Dockerfile` is equipped with all necessary build arguments for successful static file collection and runtime configuration.

#### [Scenario: Add Build ARGs to Dockerfile]
- Add `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME`, `AWS_S3_REGION_NAME`, and `STORAGE_AWS` as `ARG` and `ENV` in `Dockerfile`.
- Add `ENV`, `DEBUG`, and `ALLOWED_HOSTS` as `ARG` and `ENV` in `Dockerfile`.

### [Requirement: Synchronize Project Setup Guide]
Update the main setup guide to reflect all configuration and infrastructure improvements.

#### [Scenario: Update `docs/project-setup.md`]
- Update all code blocks and environment file examples in `docs/project-setup.md` to match the refined configuration (EMAILS_NOTIFICATIONS, AWS variables, Dockerfile ARGs).
