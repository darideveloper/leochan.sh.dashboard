# Backend API Documentation

This document provides a detailed technical reference for the REST APIs implemented in the Leochan.sh dashboard.

## Base URL
`http://localhost:8000/api/` (Development)

## 1. CV API

**Endpoint:** `/cv/`  
**Method:** `GET`  
**Permissions:** `AllowAny`  
**Description:** Retrieves the single professional profile. Since `Profile` is a singleton model, both the list and detail actions return the same object.

### Response Data Structure (`CVData`)

| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | Full name. |
| `role` | `string` | Professional title. |
| `contact` | `object` | Nested contact details. |
| `contact.email` | `string` | Email address. |
| `contact.phone` | `string` | Phone number. |
| `contact.linkedin` | `string` | LinkedIn URL. |
| `contact.drivingLicense` | `string` | Driving license status. |
| `aboutMe` | `string` | Biography. |
| `technicalSkills` | `array` | Skill categories. |
| `experience` | `array` | Work history objects. |
| `education` | `array` | Academic history objects. |
| `languages` | `array` | Spoken languages and levels. |
| `aeronautical` | `string[]` | Flattened list of aeronautical skills. |
| `interests` | `string[]` | Flattened list of interests. |
| `projects` | `array` | Projects marked as CV highlights. |

### Example Usage
```bash
curl -X GET http://localhost:8000/api/cv/
```

---

## 2. Portfolio API

### List Projects
**Endpoint:** `/projects/`  
**Method:** `GET`  
**Permissions:** `AllowAny`  
**Pagination:** Disabled (returns all projects in an array).

#### Response Data Structure (`ProjectSummary[]`)
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | Project slug. |
| `title` | `string` | Name of the project. |
| `image` | `string` | Absolute URL to the cover image. |
| `link` | `string` | Source code URL. |
| `preview` | `string` | Live demo URL. |
| `status` | `string` | Human-readable status (e.g., "Deployed"). |

### Get Project Details
**Endpoint:** `/projects/{id}/`  
**Method:** `GET`  
**Permissions:** `AllowAny`

#### Response Data Structure (`ProjectDetail`)
Inherits all fields from `ProjectSummary` plus:

| Field | Type | Description |
| :--- | :--- | :--- |
| `description` | `string` | Short summary for cards. |
| `fullDescription` | `string` | Detailed overview for the sidebar. |
| `content` | `string` | Main body content in **Markdown**. |
| `technologies` | `string[]` | Flattened list of technology names. |
| `date` | `string` | Year or date range. |

### Example Usage
```bash
# List all projects
curl -X GET http://localhost:8000/api/projects/

# Get specific project details
curl -X GET http://localhost:8000/api/projects/automated-watering-system/
```

## Technical Implementation Details

- **Framework**: Django REST Framework (DRF).
- **Serializers**: 
    - `CVDataSerializer`: Uses `SerializerMethodField` for complex nesting and string manipulation (e.g., splitting education lines).
    - `ProjectSummarySerializer` & `ProjectDetailSerializer`: Leverage `get_status_display` for labels and `SlugRelatedField` for flattening.
- **Views**: 
    - `CVViewSet`: Overrides `list` and `retrieve` to always return the singleton instance via `Profile.get_solo()`.
    - `ProjectViewSet`: Dynamically switches serializers based on the action and pre-fetches related technologies to optimize performance.
