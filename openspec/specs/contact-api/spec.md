# contact-api Specification

## Purpose
TBD - created by archiving change implement-contact-form. Update Purpose after archive.
## Requirements
### Requirement: Contact Form API Endpoint
The system SHALL expose a public POST endpoint at `/api/contact/` for receiving contact form submissions.

#### Scenario: Submit contact form
- **GIVEN** a JSON payload with `name`, `email`, and `message`
- **WHEN** a `POST` request is made to `/api/contact/`
- **THEN** it SHOULD return a 201 Created response
- **AND** it MUST create a `ContactMessage` record in the database
- **AND** it MUST trigger an email notification to the site administrator.

#### Scenario: Invalid contact form submission
- **GIVEN** a JSON payload with missing or invalid fields
- **WHEN** a `POST` request is made to `/api/contact/`
- **THEN** it SHOULD return a 400 Bad Request response with error details.

### Requirement: Contact Form Email Notification
The system SHALL notify the site administrator when a new contact message is received.

#### Scenario: Send email on submission
- **GIVEN** a successful `ContactMessage` creation
- **WHEN** the message is saved via the API
- **THEN** it MUST send an email using the `EMAIL_FROM` address
- **AND** it MUST send the email to all addresses in `EMAILS_NOTIFICATIONS`
- **AND** the subject SHOULD include the sender's name
- **AND** the body MUST contain the sender's name, email, and message.

