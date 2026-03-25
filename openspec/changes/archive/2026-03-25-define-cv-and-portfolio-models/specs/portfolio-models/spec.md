# Spec: Portfolio Models

## ADDED Requirements

### Requirement: Technology Tags
The system SHALL maintain a reusable list of technologies for tagging projects.

#### Scenario: Define Technology Model
- Model name: `Technology`.
- Fields: `name` (Char), `slug` (Slug).

### Requirement: Detailed Project Portfolio
The system SHALL store project information for showcase purposes.

#### Scenario: Define Project Model
- Model name: `Project`.
- Fields: 
  - `id`: `SlugField` (Primary Key).
  - `title`: `CharField`.
  - `image`: `URLField` or `FileField`.
  - `link`: `URLField`.
  - `preview`: `URLField`.
  - `status`: `CharField` (Choices: Deployed, In Development).
  - `description`: `CharField`.
  - `full_description`: `TextField`.
  - `content`: `TextField` (Markdown).
  - `date`: `CharField`.
  - `is_cv_highlight`: `BooleanField`.
- Relations: `ManyToMany` with `Technology`.
