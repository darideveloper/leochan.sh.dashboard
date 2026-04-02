# Design: Implement Contact Form

## Architectural Context
The `leochan.sh-dashboard` is designed as a central management system for the user's personal site and CV. The contact form is a cross-cutting concern that doesn't belong exclusively to `cv` or `portfolio`, so it will be integrated into the `shared` app.

## Proposed Changes

### Hybrid Storage & Notification
The choice to both store in a model and send an email is based on reliability:
-   **Model Storage (DB):** Serves as a "source of truth" and allows for easy management and auditing via the admin panel. Messages will never be lost due to email server issues.
-   **Email Notification:** Provides real-time alerts to the site owner without requiring them to check the admin dashboard manually.

### Model: `ContactMessage`
The model will be placed in `shared/models.py`.
-   `name`: `CharField(max_length=255)`
-   `email`: `EmailField()`
-   `message`: `TextField()`
-   `created_at`: `DateTimeField(auto_now_add=True)`

### API: Contact Endpoint
A new DRF view will handle `POST` requests at `/api/contact/`.
-   **Validation:** Use `ContactMessageSerializer` to ensure `name`, `email`, and `message` are present and valid.
-   **Permissions:** Use `rest_framework.permissions.AllowAny` to allow public submissions.
-   **Throttling:** (Optional but recommended) DRF's `AnonRateThrottle` should be applied to prevent spam.

### Email Logic
The `send_mail` call will occur in the `perform_create` method of the `CreateAPIView` (or within the `save()` method of the serializer, but keeping it in the view's flow is clearer for side effects).
-   **Subject:** `New Contact Message from {name}`
-   **Recipient:** List from `EMAILS_NOTIFICATIONS` (from `settings.py`).
-   **Backend:** Already configured to use SMTP in `settings.py`.

## Data Model Diagram (Mental Model)
`ContactMessage` (id, name, email, message, created_at)

## User Experience (Admin)
The admin will see a new "Contact Messages" section in the dashboard. Using `django-unfold`, the list view will show:
-   `name`, `email`, `created_at`
-   Filtering by date and searching by name/email.
-   Read-only fields for existing messages (typically contact messages are not edited).

## Alternatives Considered
-   **Email-only:** Faster to implement but risky (loss of data).
-   **Third-party (e.g., Formspree):** Adds an external dependency and cost; hosting it locally is preferred for a personal dashboard.
