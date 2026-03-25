# Proposal: Define CV and Portfolio Models

## Goal
Implement a robust and dry data structure for the `cv` and `portfolio` applications using Django models that align with the required frontend API data types.

## Capabilities
- **CV Data Management**: Provide a single profile model with relational lists for work experience, education, skills, and languages.
- **Project Showcase Management**: Provide models for detailed project descriptions, status tracking, and technology tagging.

## Architectural Reasoning
We are using a singleton pattern for the profile to simplify the `/cv` API endpoint and a normalized relational structure for all lists to ensure data integrity and easy administration. Projects are decoupled from the profile but integrated via a highlight flag for the CV display.

Details are documented in [design.md](./design.md).

## Related Changes
- None (Initial model definition).

## Future Consideration
- **API Implementation**: DRF serializers and viewsets will be added in a subsequent change to expose these models.
- **Admin Customization**: Specialized admin views for the singleton profile and inline sorting will be added later.
