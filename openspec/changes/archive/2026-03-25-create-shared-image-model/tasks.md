# Tasks: Create Shared Image Model

## Capabilities
- `shared-models`

## Implementation Steps

### Capability: shared-models

#### Task: Create `shared` app
- [x] Run `python manage.py startapp shared`.
- [x] Add `shared` to `INSTALLED_APPS` in `project/settings.py`.
- [x] Configure `shared/apps.py` if needed.
- [x] **Validation**: `python manage.py check`.

#### Task: Define `Image` model
- [x] Create `shared/models.py` with `Image` model fields: `name`, `image`, `upload_date`.
- [x] Set `upload_to="shared/images/"` for `image` field.
- [x] **Validation**: `python manage.py makemigrations shared && python manage.py migrate`.

#### Task: Register `Image` in Admin
- [x] Create `shared/admin.py`.
- [x] Import `unfold.admin.ModelAdmin`.
- [x] Define `ImageAdmin` with `list_display` and `search_fields`.
- [x] Implement `image_preview` helper in `ImageAdmin`.
- [x] **Validation**: Check admin interface at `/admin/shared/image/`.
