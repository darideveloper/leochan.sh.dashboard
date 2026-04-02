# Proposal: Implement Contact Form Endpoint

## Overview
This change implements a contact form endpoint at `/api/contact/` that allows users to send messages from the `leochan.sh` frontend. The implementation follows a hybrid approach: messages are stored in a `ContactMessage` model for persistence and dashboard management, and an email notification is sent to the site administrator upon each submission.

## Problem Statement
The `leochan.sh` website needs a way for visitors to reach out. Currently, there is no backend support for receiving, storing, or notifying about contact form submissions.

## Proposed Solution
1.  **Model Storage:** Add a `ContactMessage` model in the `shared` app to store `name`, `email`, and `message`.
2.  **Admin Integration:** Register the model in Django Admin using the `django-unfold` theme for easy management.
3.  **API Endpoint:** Create a public POST endpoint `/api/contact/` using Django REST Framework.
4.  **Email Notification:** Use Django's `send_mail` utility to notify the administrator (configured in `EMAILS_NOTIFICATIONS`) when a new message is received.

## Goals
- Provide a reliable way to receive contact messages.
- Ensure messages are never lost (stored in DB).
- Notify the owner immediately via email.
- Maintain consistency with the existing `shared` app and `unfold` admin style.

## Scope
-   **In-Scope:**
    - `ContactMessage` model in `shared` app.
    - DRF Serializer for validation.
    - DRF CreateAPIView with `AllowAny` permission.
    - Email sending logic on successful save.
    - Admin registration.
-   **Out-of-Scope:**
    - Spam protection (CAPTCHA) - to be added later if needed.
    - Multi-recipient management (uses existing `EMAILS_NOTIFICATIONS` setting).
