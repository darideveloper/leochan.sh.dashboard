# Tasks: Implement Django Unfold

## Phase 1: Dependencies & Settings
- [x] Add `django-unfold==0.77.1` to `requirements.txt`. (Already present)
- [x] Update `INSTALLED_APPS` in `project/settings.py` to include `unfold` apps before `django.contrib.admin`.
- [x] Add the `UNFOLD` dictionary to `project/settings.py` with branding, colors, and sidebar navigation.
- [x] Verify `UNFOLD` settings are correctly loaded via `python manage.py shell`.

## Phase 2: Callbacks & Utils
- [x] Create `utils/callbacks.py` with `environment_callback`.
- [x] Create `project/admin.py` with `UserAdmin` and `ModelAdminUnfoldBase`.
- [x] Register `User` model using `UserAdmin(BaseUserAdmin, ModelAdmin)`.

## Phase 3: Static Assets & Templates
- [x] Create `static/js/add_tailwind_styles.js`.
- [x] Create `static/js/load_markdown.js`.
- [x] Create `static/js/range_date_filter_es.js`.
- [x] Create/Update `project/templates/admin/base.html` to extend `unfold/layouts/base.html`.
- [x] Verify template overrides by checking the admin login page.

## Phase 4: Validation
- [x] Run `python manage.py collectstatic --noinput` to ensure new JS files are discovered.
- [x] Verify the admin dashboard reflects the custom `UNFOLD` settings.
