# cv-models Specification

## Purpose
TBD - created by archiving change define-cv-and-portfolio-models. Update Purpose after archive.
## Requirements
### Requirement: Singleton CV Profile
The system SHALL maintain a single profile representing the CV owner's primary details.

#### Scenario: Define Profile Model
- Model name: `Profile`.
- Base class: `solo.models.SingletonModel`.
- Fields: `name` (Char), `role` (Char), `email` (Email), `phone` (Char), `linkedin` (URL), `driving_license` (Char), `about_me` (Text).

### Requirement: CV Technical Skills
The CV data SHALL support nested technical skills grouped by category.

#### Scenario: Define SkillCategory Model
- Model name: `SkillCategory`.
- Fields: `name` (Char), `order` (Int).
- Relation: `ForeignKey` to `Profile`.

#### Scenario: Define Skill Model
- Model name: `Skill`.
- Fields: `name` (Char), `details` (Char), `order` (Int).
- Relation: `ForeignKey` to `SkillCategory`.

### Requirement: CV Work Experience
The system SHALL store professional work experiences in chronological or manual order.

#### Scenario: Define Experience Model
- Model name: `Experience`.
- Fields: `date_range` (Char), `company` (Char), `role` (Char), `order` (Int).
- Relation: `ForeignKey` to `Profile`.

### Requirement: CV Education
The system SHALL store academic achievements.

#### Scenario: Define Education Model
- Model name: `Education`.
- Fields: `date_range` (Char), `institution` (Char), `details` (Text), `order` (Int).
- Relation: `ForeignKey` to `Profile`.

### Requirement: CV Languages
The system SHALL list languages and proficiency levels.

#### Scenario: Define Language Model
- Model name: `Language`.
- Fields: `name` (Char), `level` (Char), `order` (Int).
- Relation: `ForeignKey` to `Profile`.

### Requirement: Simple List Fields
Fields for aeronautical skills and interests SHALL be included in the Profile.

#### Scenario: Add aeronautical and interests to Profile
- Fields: `aeronautical_skills` (Text/JSON), `interests` (Text/JSON).
- Implementation Note: If using SQLite, a `TextField` with newline-separated values or a `JSONField` can be used.

