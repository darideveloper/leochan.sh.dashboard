# Design: Production-Ready Configuration

## Strategy

### Environment Management
Using `python-dotenv`, the configuration will load from:
1. `.env` (main entry point, defines `ENV`).
2. `.env.{ENV}` (specific environment variables for `dev` or `prod`).

#### Proposed `.env` Content
```env
ENV=dev
SECRET_KEY=django-insecure-placeholder-change-me
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/dbname
CORS_ALLOWED_ORIGINS=http://localhost:3000
CSRF_TRUSTED_ORIGINS=http://localhost:3000
```

#### Proposed `.env.dev` Content
```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
STORAGE_AWS=False
```

#### Proposed `.env.prod` Content
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
```

### API Pagination Implementation
The `project/pagination.py` will implement a custom class to provide consistent metadata.

#### `CustomPageNumberPagination` Implementation
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

### Settings Logic Updates
The `project/settings.py` will be restructured to use the environment-variable-first approach. It will include:
- **Dynamic App Loading:** Correctly ordering `unfold` before `django.contrib.admin`.
- **Conditional Storage:** Switching between WhiteNoise/FileSystem and AWS S3 based on `STORAGE_AWS`.
- **Database Selection:** Switching between SQLite and PostgreSQL, with automatic `testing.sqlite3` for test runs.
- **REST Framework Setup:** Using the new `CustomPageNumberPagination` and setting default permissions/authentication.
- **Email Configuration:** Full SMTP support via environment variables.

### App Detection
The following local apps will be included in `INSTALLED_APPS`:
- `portfolio`
- (Any other apps discovered in the root directory)
