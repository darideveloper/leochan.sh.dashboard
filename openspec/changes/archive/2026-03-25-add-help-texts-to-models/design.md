# Design: Add help_text to Models

This design document outlines the addition of `help_text` to all Django models in the `cv` and `portfolio` apps.

## Problem Statement
The current Django admin interface lacks context for some fields, which can lead to confusion or inconsistent data entry. For example, it's not immediately clear that the `content` field in the `Project` model expects Markdown or what the expected format for `date_range` is.

## Solution
Add descriptive `help_text` to all model fields based on the `docs/frontend-apis.md` documentation. This provides on-the-spot guidance for the administrator.

## Implementation Details

### CV Models (`cv/models.py`)

| Model | Field | Proposed Help Text |
| :--- | :--- | :--- |
| **Profile** | `name` | "Full name of the profile (e.g., LÉONARD-ANTON LLOSA)." |
| | `role` | "Professional title or current position (e.g., Future Network & Security Engineer)." |
| | `email` | "Professional email address." |
| | `phone` | "Contact phone number (e.g., +33 6 62 38 65 96)." |
| | `linkedin` | "Link to your professional LinkedIn profile." |
| | `driving_license` | "Driving license status or category (e.g., Category B - Vehicle Owner)." |
| | `about_me` | "A short professional biography or 'About Me' section." |
| **AeronauticalSkill** | `name` | "Aeronautical skill, certification, or experience (e.g., LAPL Student Pilot)." |
| | `order` | "Display order (lower numbers appear first)." |
| **Interest** | `name` | "A personal interest or hobby (e.g., Aviation, Video Editing)." |
| | `order` | "Display order (lower numbers appear first)." |
| **SkillCategory** | `name` | "The name of the skill category (e.g., SYSTEMS & DEVSECOPS)." |
| | `order` | "Display order (lower numbers appear first)." |
| **Skill** | `name` | "The specific skill name (e.g., Automation)." |
| | `details` | "Additional details or tools for this skill (e.g., Ansible, n8n)." |
| | `order` | "Display order (lower numbers appear first)." |
| **Experience** | `date_range` | "The time period of the experience (e.g., 10/2025 – 08/2026)." |
| | `company` | "The name of the company or organization." |
| | `role` | "Your role or job title during this period." |
| | `order` | "Display order (lower numbers appear first)." |
| **Education** | `date_range` | "The time period of the education (e.g., 02/2024 – 06/2026)." |
| | `institution` | "The name of the school or university." |
| | `details` | "Specific details, degrees, or specializations (supports multiple lines)." |
| | `order` | "Display order (lower numbers appear first)." |
| **Language** | `name` | "The name of the language (e.g., English)." |
| | `level` | "Proficiency level (e.g., Native, TOEIC 940)." |
| | `order` | "Display order (lower numbers appear first)." |

### Portfolio Models (`portfolio/models.py`)

| Model | Field | Proposed Help Text |
| :--- | :--- | :--- |
| **Technology** | `name` | "The name of the technology (e.g., Python, React)." |
| **Project** | `id` | "Unique identifier for the project URL (slug)." |
| | `title` | "The name of the project." |
| | `image` | "Cover image for the project." |
| | `link` | "URL to the project's source code (e.g., GitHub, Gitea)." |
| | `preview` | "URL to a live demo or production site." |
| | `status` | "Current status of the project (e.g., Deployed, In Development)." |
| | `description` | "A short summary of the project for cards." |
| | `full_description` | "A detailed overview for the sidebar." |
| | `content` | "Main body content of the project page (Markdown format)." |
| | `date` | "Year or date range of the project (e.g., 2023)." |
| | `is_cv_highlight` | "If checked, this project will be highlighted in the CV section." |
| | `technologies` | "List of technologies used in this project." |

## Rationale
Using `help_text` is the standard Django way to provide documentation within the admin interface. It is lightweight, requires no additional libraries, and is easily maintainable.

## Alternatives Considered
- **Field labels**: Not suitable for longer descriptions.
- **Custom admin templates**: Overkill for just providing field-level help.
- **Internal documentation (e.g., Wiki)**: Less effective as it's not directly visible where the action takes place.
