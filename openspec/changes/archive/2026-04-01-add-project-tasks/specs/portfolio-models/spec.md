# portfolio-models Specification Delta

## ADDED Requirements

### Requirement: Project Tasks
The system SHALL store structured tasks for each project, primarily for CV highlights.

#### Scenario: Define ProjectTask Model
- Model name: `ProjectTask`.
- Fields:
  - `project`: `ForeignKey` to `Project` (related_name="tasks").
  - `description`: `CharField`. help_text="A specific task or achievement in this project (e.g., 'Coded in Arduino')."
  - `order`: `PositiveIntegerField`. help_text="Display order (lower numbers appear first)."
- Meta:
  - `ordering`: `['order']`
