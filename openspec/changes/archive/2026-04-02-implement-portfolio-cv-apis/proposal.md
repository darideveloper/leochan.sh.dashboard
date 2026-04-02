# Proposal: Implement Portfolio and CV APIs

## Why
The project requires a functional API to expose CV and Portfolio data to the frontend, as defined in `docs/frontend-apis.md`. Currently, the models exist, but no serializers, views, or endpoints are implemented.

## What Changes
- Implement `CVViewSet` in `cv/views.py` to expose profile data at `/api/cv/`.
- Implement `ProjectViewSet` in `portfolio/views.py` to expose project list and details at `/api/projects/`.
- Create `cv/serializers.py` and `portfolio/serializers.py` with custom logic to match the frontend spec (camelCase, nested objects, flattened lists).
- Update `project/urls.py` to register the new viewsets with the DRF router.
- Update `REST_FRAMEWORK` settings to allow `AllowAny` for these specific endpoints (or globally if appropriate).
- Add unit tests for all new endpoints.

## Impact
- **API**: New endpoints `/api/cv/`, `/api/projects/`, and `/api/projects/{id}/`.
- **Frontend**: Frontend applications can now consume dynamic data from the backend.
