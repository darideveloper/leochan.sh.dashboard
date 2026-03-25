# Proposal: Create Shared Image Model

This proposal introduces a new Django app named `shared` with an `Image` model to manage media assets for markdown editors and other components across the project.

## Problem
Currently, the project lacks a centralized way to manage images that are not directly tied to a specific project or profile, especially for use within markdown content where image URLs are needed.

## Solution
Create a `shared` app with a simple `Image` model. This model will store the image file, a descriptive name, and the upload timestamp. It will be registered in the Django Admin using the `django-unfold` theme for consistency.

## Capabilities
- `shared-models`: Defines the `Image` model and its admin registration.

## Relationships
- This app is independent but can be used as a source for image URLs in `portfolio` and `cv` markdown fields.
