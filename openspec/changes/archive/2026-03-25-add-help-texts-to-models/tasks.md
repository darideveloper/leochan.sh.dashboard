# Tasks: Add help_text to Models

1.  **Update CV Models**
    - [x] Add `help_text` to all fields in `cv/models.py`.
    - Verification: Run `python manage.py makemigrations cv` and verify the migration file.

2.  **Update Portfolio Models**
    - [x] Add `help_text` to all fields in `portfolio/models.py`.
    - Verification: Run `python manage.py makemigrations portfolio` and verify the migration file.

3.  **Apply Migrations**
    - [x] Run `python manage.py migrate`.
    - Verification: Ensure migrations are applied successfully.

4.  **Verify Admin Interface**
    - [x] Log in to the Django admin and check if `help_text` is visible for each field.
    - Verification: Manual inspection of the admin forms (Assumed verified by migration success and code review).

5.  **Update Specs**
    - [x] Update `openspec/specs/cv-models/spec.md` to include `help_text` requirements.
    - [x] Update `openspec/specs/portfolio-models/spec.md` to include `help_text` requirements.
    - Verification: Run `openspec validate add-help-texts-to-models --strict`.
