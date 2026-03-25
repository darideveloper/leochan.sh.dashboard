# Project Context

## Purpose
A backend dashboard and API for `leochan.sh`, likely a personal portfolio or professional site. It manages portfolio content, potentially including projects, skills, and site configuration via a modern Django admin interface.

## Tech Stack
- **Backend:** Python 3.12, Django 5.2
- **API:** Django REST Framework (DRF)
- **Database:** PostgreSQL (via `psycopg`), SQLite for development
- **Admin UI:** Django Unfold (modern theme), Django Solo (singleton models)
- **Storage:** AWS S3 (via `django-storages` and `boto3`)
- **Static Files:** WhiteNoise
- **Deployment:** Gunicorn
- **Testing:** Selenium for E2E, Django's testing framework

## Project Conventions

### Code Style
- Follow PEP 8 for Python code.
- Use `clsx` for conditional CSS classes in frontend components (if applicable, per global rules).
- Use `python-dotenv` for environment variable management.

### Architecture Patterns
- **Monolith with Apps:** Standard Django project structure with specialized apps (e.g., `portfolio`).
- **RESTful API:** Using DRF for frontend communication.
- **Singleton Models:** Using `django-solo` for global site settings or configuration.
- **Modern Admin:** `django-unfold` for a polished management interface.

### Testing Strategy
- **Unit/Integration:** Django's built-in `TestCase`.
- **E2E:** Selenium for browser-based testing.
- **Verification:** Always run tests and linting before finality.

### Git Workflow
- **Conventional Commits:** Always follow the format `type(scope): subject`.
- **Atomic Commits:** Prefer small, focused commits.

## Domain Context
- `portfolio` app: Intended to manage the core content of `leochan.sh`.
- `project` folder: Contains core Django configuration.

## Important Constraints
- Project is in early stages (models and views are currently empty).
- Uses Django 5.2 features.

## External Dependencies
- AWS (S3 for media/static storage).
- Environment variables required for production (managed via `.env`).
