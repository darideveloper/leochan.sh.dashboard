# Capability: API Configuration

Implement custom pagination for the Django REST Framework (DRF) API.

## ADDED Requirements

### Requirement: Custom Pagination
The project MUST have a `CustomPageNumberPagination` class in `project/pagination.py`.

#### Scenario: Provide Paginated Response
Given the DRF API is used
When a list request is made
Then it SHOULD return paginated results including `count`, `next`, `previous`, `page`, `page_size`, `total_pages`, and `results`.
