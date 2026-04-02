# shared-models Specification

## Purpose
TBD - created by archiving change create-shared-image-model. Update Purpose after archive.
## Requirements
### Requirement: Shared Image Model
The system SHALL provide a `shared` app with an `Image` model to store media assets.

#### Scenario: Create Image model in shared app
- **GIVEN** a new app named `shared` exists
- **WHEN** the `Image` model is defined
- **THEN** it MUST include a `name` field (`CharField`, max 255)
- **AND** it MUST include an `image` field (`ImageField`, upload_to="shared/images/")
- **AND** it MUST include an `upload_date` field (`DateTimeField`, auto_now_add=True)
- **AND** its string representation MUST return the `name`

### Requirement: Shared Admin Registration
The system SHALL register the `Image` model in the Django admin using the `django-unfold` theme.

#### Scenario: Register Image model in admin
- **GIVEN** the `Image` model exists
- **WHEN** registering it with `django-admin`
- **THEN** it MUST use `unfold.admin.ModelAdmin`
- **AND** it MUST display `name`, `upload_date`, and an image preview in the list view
- **AND** it MUST allow searching by `name`

### Requirement: App Integration
The project SHALL include the `shared` app in its `INSTALLED_APPS` configuration.

#### Scenario: Add shared app to project settings
- **GIVEN** the `shared` app is created
- **WHEN** configuring `INSTALLED_APPS` in `project/settings.py`
- **THEN** the `shared` app MUST be included in the local apps list

### Requirement: Contact Message Model
The system SHALL provide a `ContactMessage` model in the `shared` app to store contact form submissions.

#### Scenario: Define ContactMessage model
- **GIVEN** the `shared` app exists
- **WHEN** the `ContactMessage` model is defined
- **THEN** it MUST include a `name` field (`CharField`, max 255)
- **AND** it MUST include an `email` field (`EmailField`)
- **AND** it MUST include a `message` field (`TextField`)
- **AND** it MUST include a `created_at` field (`DateTimeField`, auto_now_add=True)
- **AND** its string representation SHOULD include the sender's name and email.

### Requirement: Contact Message Admin Registration
The system SHALL register the `ContactMessage` model in the Django admin using the `django-unfold` theme.

#### Scenario: Register ContactMessage in admin
- **GIVEN** the `ContactMessage` model exists
- **WHEN** registering it with `django-admin`
- **THEN** it MUST use `unfold.admin.ModelAdmin`
- **AND** it SHOULD display `name`, `email`, and `created_at` in the list view
- **AND** it SHOULD allow searching by `name` and `email`
- **AND** it SHOULD provide date hierarchy filtering by `created_at`.

