# Proposal: Add Project Tasks Model

## Problem
The `CVData` response requires a list of **tasks** (bullet points) for each project highlighted in the CV (when `is_cv_highlight` is True). Currently, the `portfolio.Project` model lacks a structured way to store these tasks, making it impossible to satisfy the frontend API requirements defined in `docs/frontend-apis.md`.

## Solution
Introduce a new `ProjectTask` model in the `portfolio` app. This model will have a `ForeignKey` relationship to the `Project` model, allowing multiple tasks to be associated with a single project. This structure will provide the necessary data for the `projects` array in the CV API response.

## Proposed Changes

### portfolio App
- **Model**: Add `ProjectTask` model.
  - `project`: `ForeignKey` to `Project` (related_name="tasks").
  - `description`: `CharField` for the task text.
  - `order`: `PositiveIntegerField` to manage display order.
- **Admin**: Register `ProjectTask` as an inline in `ProjectAdmin` for a better user experience.

## Impact
- **Database**: New table `portfolio_projecttask`.
- **API**: Enables the `projects[].tasks` field in the `/cv` endpoint.
- **Admin**: Allows users to add/edit/reorder tasks directly from the Project change page.
