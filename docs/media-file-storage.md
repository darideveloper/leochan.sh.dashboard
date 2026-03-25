# Media File Storage Integration Guide (AWS S3 & DigitalOcean Spaces)

This document provides a detailed breakdown of how to integrate and configure cloud storage for media and static files in a Django project, using **AWS S3** or **DigitalOcean Spaces**.

## 🚀 Overview

The integration relies on two primary libraries:
- **`django-storages`**: A collection of custom storage backends for Django.
- **`boto3`**: The AWS SDK for Python, which allows Django to communicate with S3-compatible APIs.

---

## 📦 Dependencies

Add the following to your `requirements.txt`:

```text
django-storages==1.14.4
boto3==1.34.162
```

---

## 🛠️ Storage Backends

To maintain separation between **Static Files**, **Public Media**, and **Private Media**, we use custom storage classes. These are defined in `nyx_dashboard/storage_backends.py`.

### Definition File: `nyx_dashboard/storage_backends.py`

```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """
    Handles static files (CSS, JS, images).
    Stored in: bucket/project_folder/static/
    """
    location = settings.STATIC_LOCATION
    default_acl = "public-read"

class PublicMediaStorage(S3Boto3Storage):
    """
    Handles public uploads (user avatars, post images).
    Stored in: bucket/project_folder/media/
    """
    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = "public-read"
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    """
    Handles sensitive files (documents, private videos).
    Stored in: bucket/project_folder/private/
    """
    location = settings.PRIVATE_MEDIA_LOCATION
    default_acl = "private"
    file_overwrite = False
    # Crucial: Private files must bypass the CDN to use Signed URLs
    custom_domain = False
```

---

## ⚙️ Django Settings Configuration

The storage logic is toggled via an environment variable `STORAGE_AWS`. 

### Configuration in `settings.py`

```python
# Storage settings
STORAGE_AWS = os.getenv("STORAGE_AWS") == "True"

if STORAGE_AWS:
    # 1. Credentials
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    # 2. Regional Settings
    # For AWS: Usually None or s3.region.amazonaws.com
    # For DigitalOcean Spaces: https://region.digitaloceanspaces.com
    AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")

    # 3. Domain/CDN settings
    # For AWS: bucket.s3.amazonaws.com
    # For DO: bucket.region.cdn.digitaloceanspaces.com (if using CDN)
    AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")

    # 4. Folder isolation
    # Allows multiple projects to share one bucket
    AWS_PROJECT_FOLDER = os.getenv("AWS_PROJECT_FOLDER")

    # 5. File Locations
    STATIC_LOCATION = f"{AWS_PROJECT_FOLDER}/static"
    PUBLIC_MEDIA_LOCATION = f"{AWS_PROJECT_FOLDER}/media"
    PRIVATE_MEDIA_LOCATION = f"{AWS_PROJECT_FOLDER}/private"

    # 6. Django-Storages Engine Mapping
    STATICFILES_STORAGE = "nyx_dashboard.storage_backends.StaticStorage"
    DEFAULT_FILE_STORAGE = "nyx_dashboard.storage_backends.PublicMediaStorage"
    PRIVATE_FILE_STORAGE = "nyx_dashboard.storage_backends.PrivateMediaStorage"

    # 7. Optimization & Security
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    AWS_DEFAULT_ACL = None
else:
    # Fallback to local storage for development
    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

---

## 🔑 Environment Variables

| Variable | Description | Example (DigitalOcean) |
| :--- | :--- | :--- |
| `STORAGE_AWS` | Toggle switch (`True`/`False`) | `True` |
| `AWS_ACCESS_KEY_ID` | Your API access key | `DO00U7QPCPCCGJ3W7QNC` |
| `AWS_SECRET_ACCESS_KEY` | Your API secret key | `QR0mj22q...` |
| `AWS_STORAGE_BUCKET_NAME`| The name of the bucket/space | `my-project-storage` |
| `AWS_PROJECT_FOLDER` | Subfolder inside the bucket | `nyx-dashboard` |
| `AWS_S3_REGION_NAME` | Cloud region | `sfo3` |
| `AWS_S3_ENDPOINT_URL` | API endpoint | `https://sfo3.digitaloceanspaces.com` |
| `AWS_S3_CUSTOM_DOMAIN` | CDN or Custom domain | `bucket.sfo3.cdn.digitaloceanspaces.com` |

---

## 🔄 Replicating in Another Project

To replicate this setup in a new Django project:

1.  **Install dependencies**: `pip install django-storages boto3`.
2.  **Create `storage_backends.py`**: Copy the class definitions provided above into your project's main module.
3.  **Update `settings.py`**:
    - Add `storages` to `INSTALLED_APPS`.
    - Copy the storage logic block.
    - Ensure `load_dotenv()` is correctly fetching variables.
4.  **Configure the Cloud Provider**:
    - Create a Bucket (S3) or Space (DO).
    - If using DigitalOcean, enable the **CDN** to get your custom domain.
    - Generate an Access Key and Secret Key.
5.  **Set Environment Variables**: Populate your `.env` file with the correct credentials.

### 💡 Pro Tip: Subdirectory Isolation
Using `AWS_PROJECT_FOLDER` is highly recommended. It allows you to use a single bucket for production, staging, and development files by simply changing the folder name in the `.env` file!
