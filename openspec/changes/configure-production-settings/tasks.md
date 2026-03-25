# Tasks: Configure Production-Ready Settings (Phased)

## Part 1: Environment Infrastructure
- [ ] Create `.env` file with `ENV=dev` and shared placeholders (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`).
- [ ] Create `.env.dev` with development-specific defaults (`DB_ENGINE=django.db.backends.sqlite3`, `STORAGE_AWS=False`).
- [ ] Create `.env.prod` with production-ready placeholders (`DB_ENGINE=django.db.backends.postgresql`, `STORAGE_AWS=True`, AWS credentials).

## Part 2: API & Pagination
- [ ] Create `project/pagination.py` and implement `CustomPageNumberPagination`.
- [ ] Implement the `get_paginated_response` method with `count`, `next`, `previous`, `page`, `page_size`, `total_pages`, and `results`.

## Part 3: Core Settings & App Integration
- [ ] Update `project/settings.py` to initialize `python-dotenv` and load environment-specific files.
- [ ] Configure `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` to read from `os.getenv`.
- [ ] Update `INSTALLED_APPS` to include `unfold` (before admin), `corsheaders`, `rest_framework`, `solo`, and local apps (`portfolio`).
- [ ] Configure `MIDDLEWARE` to include `WhiteNoiseMiddleware` and `CorsMiddleware`.

## Part 4: Database & Storage Strategy
- [ ] Implement dynamic `DATABASES` logic in `settings.py` (switching between SQLite and PostgreSQL/MySQL based on `DB_ENGINE`).
- [ ] Add `IS_TESTING` check to force `testing.sqlite3` during test runs.
- [ ] Implement conditional `STORAGES` configuration (switching between FileSystem/WhiteNoise and AWS S3 based on `STORAGE_AWS`).

## Part 5: Security, API & Email Configuration
- [ ] Configure `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS` logic.
- [ ] Add `REST_FRAMEWORK` configuration using `CustomPageNumberPagination`.
- [ ] Setup `EMAIL_BACKEND` and SMTP settings using environment variables.
- [ ] Configure global `DATE_FORMAT`, `TIME_FORMAT`, and `DATETIME_FORMAT`.

## Final Validation
- [ ] Run `python manage.py check` to verify the complete configuration.
- [ ] Run `python manage.py test` to ensure test-specific database isolation.
