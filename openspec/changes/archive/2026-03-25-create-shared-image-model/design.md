# Design: Shared Image Model

The `shared` app will be used for assets that may be reused or referenced within text fields (like markdown).

## Architecture
- **App**: `shared`
- **Model**: `Image`
  - `name`: `CharField(max_length=255)` - descriptive name.
  - `image`: `ImageField(upload_to="shared/images/")` - the actual image file.
  - `upload_date`: `DateTimeField(auto_now_add=True)` - timestamp of upload.

## Admin
- Uses `unfold.admin.ModelAdmin`.
- `list_display`: `["name", "image_preview", "upload_date"]`
- `search_fields`: `["name"]`
- `image_preview`: A helper method in `ModelAdmin` to show a small preview in the list view.

## Integration
The app will be added to `INSTALLED_APPS` in `project/settings.py`.
