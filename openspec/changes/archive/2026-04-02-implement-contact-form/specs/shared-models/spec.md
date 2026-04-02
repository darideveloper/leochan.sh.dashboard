# shared-models Specification Delta

## ADDED Requirements

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
