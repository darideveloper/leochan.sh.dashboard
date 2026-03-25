# environment Spec Delta

## ADDED Requirements

### Requirement: Production Variable Set
The project MUST define a set of environment variables for production configuration.

#### Scenario: Standardize AWS Variables
- ADDED: `AWS_S3_ENDPOINT_URL` MUST be included in the environment for S3-compatible storage providers like DigitalOcean Spaces.

#### Scenario: Standardize Email Notification Variables
- MODIFIED: `EMAILS_NOTIFICATIONS` SHOULD be the standardized variable for email recipient lists.
- REMOVED: `EMAIL_USE_TLS` SHOULD be removed in favor of `EMAIL_USE_SSL`.
