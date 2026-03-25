# portfolio-models Specification Delta

## MODIFIED Requirements

### Requirement: Technology Tags
The system SHALL maintain a reusable list of technologies for tagging projects.

#### Scenario: Define Technology Model
- Model name: `Technology`.
- Fields:
  - `name` (Char, unique): help_text="The name of the technology (e.g., Python, React)."

### Requirement: Detailed Project Portfolio
The system SHALL store project information for showcase purposes.

#### Scenario: Define Project Model
- Model name: `Project`.
- Fields:
  - `id`: `SlugField` (Primary Key). help_text="Unique identifier for the project URL (slug)."
  - `title`: `CharField`. help_text="The name of the project."
  - `image`: `FileField`. help_text="Cover image for the project."
  - `link`: `URLField`. help_text="URL to the project's source code (e.g., GitHub, Gitea)."
  - `preview`: `URLField`. help_text="URL to a live demo or production site."
  - `status`: `CharField` (Choices). help_text="Current status of the project (e.g., Deployed, In Development)."
  - `description`: `CharField`. help_text="A short summary of the project for cards."
  - `full_description`: `TextField`. help_text="A detailed overview for the sidebar."
  - `content`: `TextField` (Markdown). help_text="Main body content of the project page (Markdown format)."
  - `date`: `CharField`. help_text="Year or date range of the project (e.g., 2023)."
  - `is_cv_highlight`: `BooleanField`. help_text="If checked, this project will be highlighted in the CV section."
- Relations: `ManyToMany` with `Technology`. help_text="List of technologies used in this project."
