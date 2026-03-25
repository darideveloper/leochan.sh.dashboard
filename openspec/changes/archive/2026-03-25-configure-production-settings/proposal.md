# Proposal: Configure Production-Ready Settings and Environment (Phased Implementation)

## Summary
Update the project configuration to support multi-environment setups (dev, prod) using `python-dotenv`, AWS S3 storage, and custom API pagination. To ensure a smooth rollout, this proposal is divided into five logical parts that can be applied independently.

## Phased Approach
The configuration will be applied in the following phases:

### Phase 1: Environment Infrastructure
Creation of `.env`, `.env.dev`, and `.env.prod` files. This establishes the foundation for environment-variable-first configuration.

### Phase 2: API & Pagination
Creation of `project/pagination.py` and the `CustomPageNumberPagination` class. This sets the standard for metadata-rich API responses.

### Phase 3: Core Settings & App Integration
Refactoring `settings.py` to initialize `python-dotenv`, load the environment files, and register all required applications (`portfolio`, `unfold`, `rest_framework`, etc.) and middleware (`whitenoise`, `corsheaders`).

### Phase 4: Database & Storage Strategy
Implementation of dynamic logic in `settings.py` to switch between database engines (SQLite, PostgreSQL) and storage backends (Local, AWS S3) based on the environment.

### Phase 5: Security, API & Email Configuration
Finalizing the configuration with CORS/CSRF settings, DRF default settings (using the new pagination), SMTP email backend, and global date/time formatting.

## Goals
- Transition to environment-variable based configuration.
- Support development and production environments.
- Integrate all local apps (`portfolio`).
- Configure third-party apps and essential middleware.
- Implement custom API pagination.
- Setup dynamic database and storage selection.

## Non-Goals
- Detailed configuration of `django-unfold`.
- Implementation of apps not currently present in the project.
