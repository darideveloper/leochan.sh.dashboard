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

