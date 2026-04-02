# api Specification Delta

## ADDED Requirements

### Requirement: CV Profile Data Exposure
The system SHALL expose the CV profile data in a specific JSON structure at `/api/cv/`.

#### Scenario: Retrieve CV Data
- **GIVEN** a `Profile` exists with related skills, experience, education, and projects.
- **WHEN** a `GET` request is made to `/api/cv/`.
- **THEN** it SHOULD return a 200 OK response with a single JSON object containing:
    - `name`, `role`, `aboutMe`.
    - `contact` object (nested `email`, `phone`, `linkedin`, `drivingLicense`).
    - `technicalSkills` array of categories with their nested skills.
    - `experience`, `education`, `languages` arrays.
    - `aeronautical`, `interests` arrays of strings.
    - `projects` array of highlighted projects with their tasks.

### Requirement: Project Portfolio Exposure
The system SHALL expose project list and details at `/api/projects/`.

#### Scenario: List Projects
- **GIVEN** multiple `Project` records exist.
- **WHEN** a `GET` request is made to `/api/projects/`.
- **THEN** it SHOULD return a 200 OK response with a paginated list of project summaries (`id`, `title`, `image`, `link`, `preview`, `status`).

#### Scenario: Get Project Detail
- **GIVEN** a `Project` exists with a specific ID.
- **WHEN** a `GET` request is made to `/api/projects/{id}/`.
- **THEN** it SHOULD return a 200 OK response with the full project details, including `technologies` (array of strings) and `content` (Markdown).
