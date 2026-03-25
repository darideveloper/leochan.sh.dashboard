# Tasks: Define CV and Portfolio Models

## CV App Models
- [ ] Implement `Profile` (SingletonModel) in `cv/models.py`.
- [ ] Implement `SkillCategory` and `Skill` with ordering in `cv/models.py`.
- [ ] Implement `Experience` and `Education` with ordering in `cv/models.py`.
- [ ] Implement `Language` with ordering in `cv/models.py`.
- [ ] Validate CV models by creating migrations: `python manage.py makemigrations cv`.

## Portfolio App Models
- [ ] Implement `Technology` with `slug` in `portfolio/models.py`.
- [ ] Implement `Project` with all required fields (Slug as PK) in `portfolio/models.py`.
- [ ] Validate Portfolio models by creating migrations: `python manage.py makemigrations portfolio`.

## Finalization
- [ ] Run full migration suite: `python manage.py migrate`.
- [ ] Verify model structure in Django shell.
