# Design: Project Tasks Structure

## Overview
The `CVData` API response requires a list of projects with their associated tasks.

```json
"projects": [
  {
    "title": "Deployment of an IT Network (Homelab \"Nekocorp\")",
    "tasks": [
      "Analyzed and designed network architecture (router on a stick)",
      "Sizing, hardware selection, and cost study",
      "Installation and cabling of network equipment",
      "Configuration of IP, routing, NAT/PAT, and services (DHCP, DNS, RADIUS)",
      "Diagnostics, incident resolution, and security hardening (Firewall, IDS/IPS, SIEM)"
    ]
  }
]
```

## Data Modeling
We chose a separate `ProjectTask` model over a `JSONField` or a simple `TextField` (with split logic) for the following reasons:
1.  **Data Integrity**: Ensures each task is a discrete record.
2.  **Ease of Management**: Allows using Django Unfold's reorderable inlines in the admin.
3.  **Future Flexibility**: Each task could eventually have more metadata (e.g., skill tags) without breaking the schema.

### Schema
| Field | Type | Description |
| :--- | :--- | :--- |
| `project` | `ForeignKey` | Relation to `Project` model. |
| `description` | `CharField` | The text content of the task (e.g., "Analyzed and designed network architecture"). |
| `order` | `PositiveIntegerField` | Used for ordering tasks in the UI and API. |

## Admin Integration
`ProjectTask` will be implemented as a `TabularInline` (or Unfold equivalent) within the `ProjectAdmin`. This allows the user to manage tasks directly while editing a project, especially those marked with `is_cv_highlight`.
