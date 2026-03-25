# Tasks: Configure Production-Ready Settings (Phased)

## Part 1: Environment Infrastructure
- [x] Create `.env` file with `ENV=dev` and shared placeholders (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`).
- [x] Create `.env.dev` with development-specific defaults (`DB_ENGINE=django.db.backends.sqlite3`, `STORAGE_AWS=False`).
- [x] Create `.env.prod` with production-ready placeholders (`DB_ENGINE=django.db.backends.postgresql`, `STORAGE_AWS=True`, AWS credentials).

## Part 2: API & Pagination
- [x] Create `project/pagination.py` and implement `CustomPageNumberPagination`.
- [x] Implement the `get_paginated_response` method with `count`, `next`, `previous`, `page`, `page_size`, `total_pages`, and `results`.

## Part 3: Core Settings & App Integration
- [x] Update `project/settings.py` to initialize `python-dotenv` and load environment-specific files.
- [x] Configure `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` to read from `os.getenv`.
- [x] Update `INSTALLED_APPS` to include `unfold` (before admin), `corsheaders`, `rest_framework`, `solo`, and local apps (`portfolio`).
- [x] Configure `MIDDLEWARE` to include `WhiteNoiseMiddleware` and `CorsMiddleware`.

## Part 4: Database & Storage Strategy
- [x] Implement dynamic `DATABASES` logic in `settings.py` (switching between SQLite and PostgreSQL/MySQL based on `DB_ENGINE`).
- [x] Add `IS_TESTING` check to force `testing.sqlite3` during test runs.
- [x] Implement conditional `STORAGES` configuration (switching between FileSystem/WhiteNoise and AWS S3 based on `STORAGE_AWS`).

## Part 5: Security, API & Email Configuration
- [x] Configure `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS` logic.
- [x] Add `REST_FRAMEWORK` configuration using `CustomPageNumberPagination`.
- [x] Setup `EMAIL_BACKEND` and SMTP settings using environment variables.
- [x] Configure global `DATE_FORMAT`, `TIME_FORMAT`, and `DATETIME_FORMAT`.

## Final Validation
- [x] Run `python manage.py check` to verify the complete configuration.
- [x] Run `python manage.py test` to ensure test-specific database isolation.
