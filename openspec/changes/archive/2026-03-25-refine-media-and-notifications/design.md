# Design: Refine Media and Notifications Configuration

This design ensures the project's media, notification, and deployment configurations are consistent, secure, and properly documented. It addresses instructions to unify variables, remove legacy settings, enhance the Docker build process, and correct comprehensive setup guides.

## Decisions

### 1. Unified Notification Variable
- **Standardization:** Standardize on `EMAILS_NOTIFICATIONS` across `settings.py`, `.env.dev`, `.env.prod`, and all documentation.

### 2. Standardizing Storage Backend Support
- **Infrastructure:** Add `AWS_S3_ENDPOINT_URL` to `.env.prod` to support S3-compatible providers.
- **Initialization:** Explicitly include `"storages"` in `INSTALLED_APPS` to ensure `django-storages` is fully integrated.

### 3. Documentation Alignment
- **Project Scope:** Update `docs/media-file-storage.md` and `docs/project-setup.md` to use the current project name (`project`) and modern settings (the `STORAGES` dictionary).

### 4. Simplified Email Configuration
- **Security:** Remove `EMAIL_USE_TLS` (Port 587) in favor of the requested `EMAIL_USE_SSL` (Port 465) for simplicity and production consistency.

### 5. Dockerfile Robustness
- **Build-Time Storage:** Add missing `AWS_*` ARGs to the `Dockerfile`. This is essential because `python manage.py collectstatic` is executed during the Docker build; without these credentials, the build will fail if `STORAGE_AWS=True` is active.
- **Runtime Context:** Add `ENV`, `DEBUG`, and `ALLOWED_HOSTS` to the `Dockerfile` to match the reference project and provide better control over the containerized environment.

## Architecture Impact
The changes impact the deployment pipeline (Dockerfile), configuration management (settings/env), and developer experience (documentation). There are no changes to the application's domain logic.

## Validation
- **Environment Check:** Verify `EMAILS_NOTIFICATIONS` is correctly loaded.
- **Build Check:** Ensure `docker build` (simulated by checking ARGs/ENVs) has access to all required configuration.
- **Configuration Check:** Run `python manage.py check` to confirm settings validity.
