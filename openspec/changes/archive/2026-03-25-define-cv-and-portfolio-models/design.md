# Design: CV and Portfolio Models

## Goal
Implement the core data models for the `cv` and `portfolio` apps to satisfy frontend API requirements for dynamic resume content and project showcases.

## Architectural Overview

### App Distribution
To maintain a clean separation of concerns:
- **`cv` app**: Manages professional profile data, education, work experience, skills, and personal information.
- **`portfolio` app**: Manages the showcase of projects, technology tags, and case study content.

### Model Strategy: CV App
The CV requires a single source of truth for the profile (name, contact) and ordered lists for professional details.

1. **Profile (Singleton)**: Use `django-solo`'s `SingletonModel` for the main CV entry. This ensures only one profile exists.
2. **Normalized Lists**: `Experience`, `Education`, and `Skill` will be separate models with a `ForeignKey` to the `Profile`.
3. **Ordering**: Each list model will include an `order` field (integer) to allow manual sorting in the admin.
4. **Skills Nesting**: `SkillCategory` (e.g., "DevOps") will group individual `Skill` entries (e.g., "Ansible").

### Model Strategy: Portfolio App
The portfolio showcases projects that may or may not be highlighted on the CV.

1. **Project Model**: Includes fields for titles, images (URLs/Paths), links, and Markdown content.
2. **Slug as Identifier**: Uses a `SlugField` to provide SEO-friendly URLs that match frontend expectation (e.g., `/projects/my-project`).
3. **Technology Tags**: A many-to-many relationship with a `Technology` model to avoid data duplication.
4. **CV Integration**: A boolean `is_cv_highlight` field allows projects to be pulled into the CV API response.

## Data Schema Summary

### CV App
- **Profile**: `name`, `role`, `email`, `phone`, `linkedin`, `driving_license`, `about_me`, `aeronautical_skills`, `interests`.
- **Experience**: `profile` (FK), `date_range`, `company`, `role`, `order`.
- **Education**: `profile` (FK), `date_range`, `institution`, `details`, `order`.
- **SkillCategory**: `profile` (FK), `name`, `order`.
- **Skill**: `category` (FK), `name`, `details`, `order`.
- **Language**: `profile` (FK), `name`, `level`, `order`.

### Portfolio App
- **Technology**: `name`, `slug`.
- **Project**: `slug`, `title`, `image_url`, `link`, `preview_url`, `status`, `short_description`, `full_description`, `content` (Markdown), `date_range`, `is_cv_highlight`, `technologies` (MTM).

## Alternatives Considered
- **JSONField**: Rejected in favor of relational models to ensure better data validation, easier admin management, and future-proof querying.
- **Unified App**: Rejected because CV and Portfolio, while related, represent different business domains (Professional Profile vs. Project Portfolio).
