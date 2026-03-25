# Project Setup Guide

Follow these steps to set up the `leochan.sh.dashboard` project from scratch.

### 1. Add requirements.txt
Create a `requirements.txt` file in the root directory with the following dependencies:

```text
# base
Django>=5.2,<5.3           # Core web framework
whitenoise>=6.11.0          # Static file serving for production
gunicorn>=24.1.1           # Production WSGI server
django-cors-headers>=4.9.0 # CORS handling for API access
python-dotenv>=1.0.1      # Environment variable management

# db
psycopg>=3.2.3             # PostgreSQL database adapter

# images
pillow>=11.1.0             # Image processing library

# drf & jwt
djangorestframework>=3.16.1 # REST API toolkit
django-filter>=24.3        # Dynamic API filtering

# testing
selenium>=4.40.0           # Browser automation for E2E tests

# admin
django-unfold==0.77.1      # Modern Django admin theme
django-solo>=2.3.0         # Singleton models for configuration

# tools
requests>=2.32.3           # HTTP library for external API calls

# storage
django-storages==1.14.4    # Custom storage backends (S3, etc.)
boto3==1.34.162            # AWS SDK for Python
```

### 2. Initial Commands
Run the following commands to initialize the environment and install dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Linux/macOS)
source venv/bin/activate

# Activate virtual environment (Windows)
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Django project
django-admin startproject project .
```

### 3. Create Initial App
Once the project is initialized, create the main application. 

> **Important:** The `{app_name}` should **ALWAYS** be prompted/requested from the user before executing this command.

```bash
python manage.py startapp {app_name}
```

### 4. Git Initialization
Initialize a Git repository to track your changes and commit the initial project state.

```bash
# Initialize git
git init

# Create .gitignore file
cat <<EOF > .gitignore
__pycache__
*__pycache__
*temp.*
temp.*
*.log*
*.zip
venv
.env
debug.*
db.*
*.sqlite3
*.pyc
credentials.json
staticfiles/
info.txt
/media
.env*
.vscode
*/.DS_Store 
.DS_Store
/docs 
*.temp
.windsurf/
EOF

# Add all files and commit
git add .
git commit -m "initial project"
```

### 5. Environment Infrastructure
Establish the foundation for environment-variable-first configuration by creating the following files in the project root.

> **Note:** If the project does not require email functionality, you can skip the `EMAIL_*` variables in the `.env.dev` and `.env.prod` files.
> **Note:** The `SECRET_KEY` should be a randomly generated string of at least 30 characters.

**`.env`** (Main entry point)
```env
ENV=dev
SECRET_KEY=django-insecure-placeholder-change-me
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
CSRF_TRUSTED_ORIGINS=http://localhost:3000
```

**`.env.dev`** (Local development defaults)
```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
STORAGE_AWS=False

EMAILs_NOTIFICATIONS=admin@example.com
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=user@example.com
EMAIL_HOST_PASSWORD=password
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
```

**`.env.prod`** (Production-ready placeholders)
```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=leochan_db
DB_USER=admin
DB_PASSWORD=secure-password
DB_HOST=db-host
DB_PORT=5432
STORAGE_AWS=True
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
AWS_S3_REGION_NAME=us-east-1
AWS_PROJECT_FOLDER=leochan-sh

EMAILs_NOTIFICATIONS=admin@example.com
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=user@example.com
EMAIL_HOST_PASSWORD=password
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
```

### 6. Core Settings & App Integration
Refactor `project/settings.py` to initialize `python-dotenv`, load environment files, and register apps/middleware.

**Initialize Dotenv at the top of `settings.py`:**
```python
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env first to get ENV value
load_dotenv(BASE_DIR / '.env')
ENV = os.getenv('ENV', 'dev')

# Load environment-specific file
load_dotenv(BASE_DIR / f'.env.{ENV}')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
```

**Update `INSTALLED_APPS` and `MIDDLEWARE`:**
- Include `corsheaders`, `rest_framework`, and `solo`.
- **Add your local application:** Include the `{app_name}` you created in Step 3 in `INSTALLED_APPS`.
- Add `CorsMiddleware` and `WhiteNoiseMiddleware` to `MIDDLEWARE`.

### 7. Database & Storage Strategy
Implement dynamic logic in `settings.py` to switch backends based on the environment.

**Dynamic Database Selection:**
```python
import sys
IS_TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

if IS_TESTING:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "testing.sqlite3"),
        }
    }
else:
    options = {}
    if os.environ.get("DB_ENGINE") == "django.db.backends.mysql":
        options = {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
        }
    
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get("DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.environ.get("DB_USER", ""),
            "PASSWORD": os.environ.get("DB_PASSWORD", ""),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", ""),
            "OPTIONS": options,
        }
    }
```

**Internationalization:**
> **Note:** Prompt the user for their preferred time zone. Default is `America/Mexico_City`.

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = "America/Mexico_City"
USE_I18N = True
USE_TZ = True
```

**Static & Media Management:**
```python
STATIC_URL = 'static/'
MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

**Conditional Storage (AWS S3 vs Local):**
```python
STORAGE_AWS = os.getenv("STORAGE_AWS") == "True"

if STORAGE_AWS:
    # AWS S3 Configuration
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
    AWS_PROJECT_FOLDER = os.getenv("AWS_PROJECT_FOLDER")

    STORAGES = {
        "default": {
            "BACKEND": "project.storage_backends.PublicMediaStorage",
        },
        "staticfiles": {
            "BACKEND": "project.storage_backends.StaticStorage",
        },
        "private": {
            "BACKEND": "project.storage_backends.PrivateMediaStorage",
        },
    }
else:
    # Local Storage Configuration
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
```

### 8. Project Assets & Customizations
Create the following directories and files to support cloud storage, admin overrides, and styling.

#### project/pagination.py
Implement custom pagination to provide metadata-rich API responses.
```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'page': self.page.number,
            'page_size': self.get_page_size(self.request),
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
```

#### project/storage_backends.py
Defines custom storage backends for S3 integration.
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """Handles static files (CSS, JS, images)."""
    location = settings.STATIC_LOCATION
    default_acl = "public-read"

class PublicMediaStorage(S3Boto3Storage):
    """Handles public uploads (user avatars, post images)."""
    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = "public-read"
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    """Handles sensitive files (documents, private videos)."""
    location = settings.PRIVATE_MEDIA_LOCATION
    default_acl = "private"
    file_overwrite = False
    custom_domain = False
```

#### project/templates/admin/base.html
Overrides the Django admin base template to include external libraries (e.g., SimpleMDE).
```html
{% extends "admin/base.html" %} {% load static %} {% block extrahead %}
{{block.super }}
<!-- Load markdown libraries -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css"
/>
<script src="https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js"></script>
{% endblock %}
```

#### static/js/add_tailwind_styles.js
Dynamically adds Tailwind CSS classes to specific elements.
```javascript
// Insert talwind code to specific html elements

// Run on load
document.addEventListener("DOMContentLoaded", () => {
  const classes = [
    {
      selector: ".btn",
      classes: "bg-primary-600 block border border-transparent cursor-pointer font-medium px-3 py-2 rounded-default text-white w-full lg:w-auto flex items-center justify-center hover:bg-primary-700 hover:text-white transition-colors duration-300",
    },
    {
      selector: ".img-preview",
      classes: "w-auto h-16 rounded-xl object-cover",
    },
  ]
  for (const elem_data of classes) {
    const { selector, classes } = elem_data
    const elems = document.querySelectorAll(selector)
    elems.forEach((elem) => {
      elem.classList.add(...classes.split(" "))
    })
  }
})
```

#### static/js/copy_clipboard.js
Handles copying URLs to the clipboard based on cookies.
```javascript
// clipboard_handler.js
document.addEventListener('DOMContentLoaded', () => {
  const getCookie = (name) => {
    const value = `; ${document.cookie}`
    const parts = value.split(`; ${name}=`)
    if (parts.length === 2) {
      let cookieValue = decodeURIComponent(parts.pop().split(';').shift())
      // Remove surrounding quotes if they exist
      return cookieValue.replace(/^"|"$/g, '')
    }
  }

  const url = getCookie('copy_to_clipboard')
  if (url) {
    navigator.clipboard.writeText(url).then(() => {
      // Clear the cookie
      document.cookie = "copy_to_clipboard=; path=/; Max-Age=-99999999;"
    })
  }
})
```

#### static/js/load_markdown.js
Initializes SimpleMDE for specific text areas.
```javascript
// Runs script when page loads
document.addEventListener("DOMContentLoaded", () => {
  // Get text areas
  const noMarkdownIds = [
    "google_maps_src", // Property google maps src field
    "description", // Post description field
  ]
  let textAreasSelector = 'div > textarea'
  const notSelector = noMarkdownIds.map(id => `:not(#id_${id})`).join("")
  textAreasSelector = `div > textarea${notSelector}`
  const textAreas = document.querySelectorAll(textAreasSelector)
  console.log({ textAreas })

  setTimeout(() => {
    textAreas.forEach(textArea => {
      new SimpleMDE({
        element: textArea,
        toolbar: [
          "bold", "italic", "heading", "|",
          "quote", "code", "link", "image", "|",
          "unordered-list", "ordered-list", "|",
          "undo", "redo", "|",
          "preview",
        ],
        spellChecker: false,
      })
    })
  }, 100)
})
```

#### static/js/range_date_filter_es.js
Updates placeholder text for date filters.
```javascript
// Update placeholder text for unfold range date filter

// Run after page loads
document.addEventListener("DOMContentLoaded", function () {
  const texts = [
    {
      names: ["created_at_from", "updated_at_from"],
      text: "Desde",
    },
    {
      names: ["created_at_to", "updated_at_to"],
      text: "Hasta",
    },
  ]

  texts.forEach((text) => {
    text.names.forEach((name) => {
      const elem = document.querySelector(`[name="${name}"]`)
      if (!elem) return
      elem.placeholder = text.text
    })
  })
})
```

#### static/js/script.js
General-purpose JavaScript logic (empty by default).
```javascript
// Add custom project-wide JavaScript here
```

#### Other Required Files
- **static/css/style.css**: Create an empty file for custom CSS.
- **static/logo.svg** and **static/favicon.png**: Add your project's logo and favicon.
- **media/**: Create an empty directory in the root for local file uploads.

### 9. Security, API & Email Configuration
Finalize the configuration with security headers, DRF defaults, and SMTP settings.

> **Note:** Prompt the user to confirm if the project needs to send emails. If emails are not required, skip the **Email SMTP Configuration** subsection below and the corresponding environment variables in Step 5.

**CORS & CSRF Configuration:**
```python
cors_allowed = os.getenv("CORS_ALLOWED_ORIGINS")
if cors_allowed and cors_allowed != "None":
    CORS_ALLOWED_ORIGINS = [
        origin.strip().rstrip("/") for origin in cors_allowed.split(",") if origin.strip()
    ]

csrf_trusted = os.getenv("CSRF_TRUSTED_ORIGINS")
if csrf_trusted and csrf_trusted != "None":
    CSRF_TRUSTED_ORIGINS = [
        origin.strip().rstrip("/") for origin in csrf_trusted.split(",") if origin.strip()
    ]
```

**Django REST Framework Setup:**
```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "project.pagination.CustomPageNumberPagination",
    "PAGE_SIZE": 12,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}
```

**Global DateTime Formatting:**

```python
DATE_FORMAT = "d/b/Y"
TIME_FORMAT = "H:i"
DATETIME_FORMAT = f"{DATE_FORMAT} {TIME_FORMAT}"
```

**Email SMTP Configuration:**
> **Note:** Skip this subsection if the project does not require email functionality.

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS") == "True"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL") == "True"
EMAIL_FROM = EMAIL_HOST_USER
EMAILS_NOTIFICATIONS = os.getenv("EMAILS_LEADS_NOTIFICATIONS", "").split(",")
```

### 10. Validation
Verify the project configuration and ensure that the test environment is correctly isolated.

```bash
# Verify the complete configuration
python manage.py check

# Run tests to ensure test-specific database isolation
python manage.py test
```

### 11. OpenSpec Setup (Gemini CLI)
Initialize and configure OpenSpec to manage project context and change proposals with Gemini CLI.

```bash
openspec init
```

After initialization, run the following command in Gemini CLI to populate your project context:

> "Please read openspec/project.md and help me fill it out with details about my project, tech stack, and conventions"
