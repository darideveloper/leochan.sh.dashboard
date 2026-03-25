# Tasks: Refine Media and Notifications Configuration

## 1. Environment and Configuration Refinement
- [x] Add `"storages"` to `INSTALLED_APPS` in `project/settings.py`.
- [x] Rename `EMAILS_LEADS_NOTIFICATIONS` to `EMAILS_NOTIFICATIONS` in `project/settings.py`.
- [x] Remove `EMAIL_USE_TLS` logic from `project/settings.py`.
- [x] Ensure `EMAIL_USE_SSL` remains active in `project/settings.py`.

## 2. Environment Files Update
- [x] Update `.env.prod`:
    - [x] Replace `EMAILs_NOTIFICATIONS` with `EMAILS_NOTIFICATIONS`.
    - [x] Remove `EMAIL_USE_TLS` (if present).
    - [x] Add `AWS_S3_ENDPOINT_URL`.
- [x] Update `.env.dev`:
    - [x] Replace `EMAILs_NOTIFICATIONS` with `EMAILS_NOTIFICATIONS`.
    - [x] Remove `EMAIL_USE_TLS` (if present).

## 3. Dockerfile Enhancement
- [x] Add the following `ARGs` and `ENVs` to `Dockerfile` before the `collectstatic` step:
    - [x] `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME`, `AWS_S3_REGION_NAME`, `AWS_S3_ENDPOINT_URL`, `AWS_S3_CUSTOM_DOMAIN`, `STORAGE_AWS`.
    - [x] `ENV`, `DEBUG`, `ALLOWED_HOSTS`.

## 4. Documentation Alignment
- [x] Update `docs/media-file-storage.md`:
    - [x] Replace `nyx_dashboard` with `project`.
    - [x] Update storage settings code examples to use the `STORAGES` dictionary.
    - [x] Add `"storages"` to `INSTALLED_APPS` in the guide.
- [x] Update `docs/project-setup.md`:
    - [x] Update `.env.dev` and `.env.prod` examples to use `EMAILS_NOTIFICATIONS`.
    - [x] Add `AWS_S3_ENDPOINT_URL` to the `.env.prod` example.
    - [x] Remove `EMAIL_USE_TLS` from email settings and environment examples.
    - [x] Update the `Dockerfile` code block with the new `ARGs` and `ENVs`.
    - [x] Ensure the `settings.py` snippet for `EMAILS_NOTIFICATIONS` matches the new variable name.

## 5. Validation
- [x] Run `python manage.py check` to verify the configuration.
- [x] Run `python manage.py collectstatic --dry-run` to ensure storage backend initialization.
