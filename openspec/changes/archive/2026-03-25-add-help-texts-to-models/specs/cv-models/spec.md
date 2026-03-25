# cv-models Specification Delta

## MODIFIED Requirements

### Requirement: Singleton CV Profile
The system SHALL maintain a single profile representing the CV owner's primary details.

#### Scenario: Define Profile Model
- Model name: `Profile`.
- Base class: `solo.models.SingletonModel`.
- Fields:
  - `name` (Char): help_text="Full name of the profile (e.g., LÉONARD-ANTON LLOSA)."
  - `role` (Char): help_text="Professional title or current position (e.g., Future Network & Security Engineer)."
  - `email` (Email): help_text="Professional email address."
  - `phone` (Char): help_text="Contact phone number (e.g., +33 6 62 38 65 96)."
  - `linkedin` (URL): help_text="Link to your professional LinkedIn profile."
  - `driving_license` (Char): help_text="Driving license status or category (e.g., Category B - Vehicle Owner)."
  - `about_me` (Text): help_text="A short professional biography or 'About Me' section."

### Requirement: CV Technical Skills
The CV data SHALL support nested technical skills grouped by category.

#### Scenario: Define SkillCategory Model
- Model name: `SkillCategory`.
- Fields:
  - `name` (Char): help_text="The name of the skill category (e.g., SYSTEMS & DEVSECOPS)."
  - `order` (Int): help_text="Display order (lower numbers appear first)."
- Relation: `ForeignKey` to `Profile`.

#### Scenario: Define Skill Model
- Model name: `Skill`.
- Fields:
  - `name` (Char): help_text="The specific skill name (e.g., Automation)."
  - `details` (Char): help_text="Additional details or tools for this skill (e.g., Ansible, n8n)."
  - `order` (Int): help_text="Display order (lower numbers appear first)."
- Relation: `ForeignKey` to `SkillCategory`.

### Requirement: CV Work Experience
The system SHALL store professional work experiences in chronological or manual order.

#### Scenario: Define Experience Model
- Model name: `Experience`.
- Fields:
  - `date_range` (Char): help_text="The time period of the experience (e.g., 10/2025 – 08/2026)."
  - `company` (Char): help_text="The name of the company or organization."
  - `role` (Char): help_text="Your role or job title during this period."
  - `order` (Int): help_text="Display order (lower numbers appear first)."
- Relation: `ForeignKey` to `Profile`.

### Requirement: CV Education
The system SHALL store academic achievements.

#### Scenario: Define Education Model
- Model name: `Education`.
- Fields:
  - `date_range` (Char): help_text="The time period of the education (e.g., 02/2024 – 06/2026)."
  - `institution` (Char): help_text="The name of the school or university."
  - `details` (Text): help_text="Specific details, degrees, or specializations (supports multiple lines)."
  - `order` (Int): help_text="Display order (lower numbers appear first)."
- Relation: `ForeignKey` to `Profile`.

### Requirement: CV Languages
The system SHALL list languages and proficiency levels.

#### Scenario: Define Language Model
- Model name: `Language`.
- Fields:
  - `name` (Char): help_text="The name of the language (e.g., English)."
  - `level` (Char): help_text="Proficiency level (e.g., Native, TOEIC 940)."
  - `order` (Int): help_text="Display order (lower numbers appear first)."
- Relation: `ForeignKey` to `Profile`.

## ADDED Requirements

### Requirement: Aeronautical Skills
The system SHALL store aeronautical skills or certifications.

#### Scenario: Define AeronauticalSkill Model
- Model name: `AeronauticalSkill`.
- Fields:
  - `name` (Char): help_text="Aeronautical skill, certification, or experience (e.g., LAPL Student Pilot)."
  - `order` (Int): help_text="Display order (lower numbers appear first)."
- Relation: `ForeignKey` to `Profile`.

### Requirement: Interests
The system SHALL store personal interests and hobbies.

#### Scenario: Define Interest Model
- Model name: `Interest`.
- Fields:
  - `name` (Char): help_text="A personal interest or hobby (e.g., Aviation, Video Editing)."
  - `order` (Int): help_text="Display order (lower numbers appear first)."
- Relation: `ForeignKey` to `Profile`.
