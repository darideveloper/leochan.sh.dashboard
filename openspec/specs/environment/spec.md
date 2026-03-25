# environment Specification

## Purpose
TBD - created by archiving change configure-production-settings. Update Purpose after archive.
## Requirements
### Requirement: Multi-Environment Files
The project MUST have three environment configuration files:
1. `.env`: Main file with `ENV=dev`.
2. `.env.dev`: Local development variables.
3. `.env.prod`: Production variables.

#### Scenario: Define ENV in .env
Given a `.env` file exists at the project root
When `settings.py` is initialized
Then it SHOULD load the value of `ENV` from `.env`.

#### Scenario: Load Environment-Specific Variables
Given `ENV` is set to `dev` in `.env`
When `settings.py` is initialized
Then it SHOULD load additional variables from `.env.dev`.

### Requirement: Production Variable Set
The project MUST define a set of environment variables for production configuration.

#### Scenario: Standardize AWS Variables
- ADDED: `AWS_S3_ENDPOINT_URL` MUST be included in the environment for S3-compatible storage providers like DigitalOcean Spaces.

#### Scenario: Standardize Email Notification Variables
- MODIFIED: `EMAILS_NOTIFICATIONS` SHOULD be the standardized variable for email recipient lists.
- REMOVED: `EMAIL_USE_TLS` SHOULD be removed in favor of `EMAIL_USE_SSL`.

