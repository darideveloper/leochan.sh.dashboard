# Tasks: Define CV and Portfolio Models

## CV App Models
- [x] Implement `Profile` (SingletonModel) in `cv/models.py`.
- [x] Implement `SkillCategory` and `Skill` with ordering in `cv/models.py`.
- [x] Implement `Experience` and `Education` with ordering in `cv/models.py`.
- [x] Implement `Language` with ordering in `cv/models.py`.
- [x] Validate CV models by creating migrations: `python manage.py makemigrations cv`.

## Portfolio App Models
- [x] Implement `Technology` with `slug` in `portfolio/models.py`.
- [x] Implement `Project` with all required fields (Slug as PK) in `portfolio/models.py`.
- [x] Validate Portfolio models by creating migrations: `python manage.py makemigrations portfolio`.

## Finalization
- [x] Run full migration suite: `python manage.py migrate`.
- [x] Verify model structure in Django shell.
