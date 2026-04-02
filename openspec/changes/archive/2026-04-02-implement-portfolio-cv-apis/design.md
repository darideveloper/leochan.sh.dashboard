# Design: Portfolio and CV APIs

## Overview
The goal is to provide a clean REST API that matches the requirements in `docs/frontend-apis.md`. The implementation will focus on transforming Django models into the specific JSON structure required by the frontend using DRF Serializers.

## Tech Stack
- Django REST Framework (DRF)
- `rest_framework.serializers.ModelSerializer`

## Data Mapping Strategy

### 1. CV Data (`/api/cv/`)
The response will be a single object (since `Profile` is a singleton).
- **CamelCase**: Field names like `driving_license` will be mapped to `drivingLicense`.
- **Nesting**: `email`, `phone`, `linkedin`, and `drivingLicense` will be nested under a `contact` object.
- **Flattening**:
    - `technicalSkills`: Grouped by `SkillCategory`.
    - `experience`: Mapped to arrays of objects with `date`, `company`, and `role`.
    - `education`: Mapped to arrays of objects. The `details` TextField will be split by newlines into an array of strings to match the frontend's `string[]` requirement.
    - `aeronautical`, `interests`: Related models flattened to arrays of strings.
    - `languages`: Array of objects (`name`, `level`).
    - `projects`: Filtered by `is_cv_highlight=True` and including a list of related `ProjectTask` descriptions.

### 2. Projects Portfolio (`/api/projects/`)
- **List View**: Returns `ProjectSummary` (subset of fields).
- **Detail View**: Returns `ProjectDetail` (all fields + technologies + content).
- **Technologies**: Flattened to an array of technology names.
- **Status Mapping**: The `status` field will return the human-readable label (e.g., "Deployed", "In Development") rather than the choice key.
- **Media URLs**: The `image` field will return the absolute URL (including protocol and host) by utilizing the serializer's `request` context.

## Permissions
Currently, `REST_FRAMEWORK` defaults to `IsAuthenticated`. Since these are public-facing portfolio APIs, we will override the permission classes for these specific viewsets to `AllowAny`.

## Testing
- **Unit Tests**: Using `rest_framework.test.APITestCase`.
- **Coverage**:
    - Verify `/api/cv/` returns the correct nested and flattened structure.
    - Verify `/api/projects/` returns the correct list of summaries.
    - Verify `/api/projects/{id}/` returns the full detail for a valid project.
    - Verify 404 behavior for invalid project IDs.
