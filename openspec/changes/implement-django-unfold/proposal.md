# Proposal: Implement Django Unfold

## Problem
The current Django Admin interface uses the default theme, which is not aligned with the modern, responsive design goals of the leochan.sh dashboard. A more customizable and aesthetically pleasing admin interface is needed for efficient content management.

## Proposed Solution
Integrate `django-unfold`, a modern and responsive Django Admin theme. This involves:
- Updating `requirements.txt` with `django-unfold`.
- Configuring `INSTALLED_APPS` and the `UNFOLD` dictionary in `settings.py`.
- Adding custom callbacks for environment-specific badges.
- Adding custom static assets (JS) to enhance the admin interface with Tailwind CSS and SimpleMDE.
- Overriding the base admin template to include these custom assets.
- Customizing the Auth models and creating a base `ModelAdminUnfoldBase` class.

## Capabilities
### Settings Integration
Update `settings.py` to include `unfold` apps and configuration.

### Admin Customization
Customize the admin interface using `unfold` features like row actions and custom callbacks.

### Enhanced UI
Add support for SimpleMDE (Markdown) and custom Tailwind-based styling in the admin.
