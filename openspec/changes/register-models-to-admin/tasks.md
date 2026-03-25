# Tasks: Register CV and Portfolio Models to Admin

## Implementation
### App: CV Admin Registration
- [x] Register `Profile` with `SingletonModelAdmin` in `cv/admin.py`.
- [x] Register `SkillCategory` and `Skill` with `TabularInline` in `cv/admin.py`.
- [x] Register `Experience`, `Education`, and `Language` in `cv/admin.py` with `list_display` and `search_fields`.

### App: Portfolio Admin Registration
- [x] Register `Technology` in `portfolio/admin.py`.
- [x] Register `Project` in `portfolio/admin.py` with `list_display`, `list_filter`, and `search_fields`.

### App: Admin Settings
- [x] Update `project/settings.py` to remove `UNFOLD['SIDEBAR']['navigation']`.
- [x] Set `UNFOLD['SIDEBAR']['show_all_applications'] = True` in `project/settings.py`.

## Validation
- [x] Verify that `admin/` page loads correctly without `NoReverseMatch`.
- [x] Confirm all `cv` and `portfolio` models are visible in the sidebar.
- [x] Verify `Profile` is manageable as a singleton.
- [x] Verify `Skill` can be edited as an inline within `SkillCategory`.
- [x] Confirm filters and search fields work as expected in `Project` admin.
